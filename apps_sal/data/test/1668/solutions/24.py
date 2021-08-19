import sys
import os
3


def main():
    T = read_int()
    for _ in range(T):
        N = read_int()
        (c, ans) = solve(N, [read_int() for _ in range(N)])
        print(c)
        for a in ans:
            print('{:04}'.format(a))


def solve(N, P):
    d = {}
    for p in P:
        if p not in d:
            d[p] = 0
        d[p] += 1
    c = 0
    ans = []
    for p in P:
        if d[p] == 1:
            ans.append(p)
            continue
        c += 1
        np = -1
        a = [p % 10, p // 10 % 10, p // 100 % 10, p // 1000]
        for i in range(4):
            for j in range(10):
                if a[i] == j:
                    continue
                orig = a[i]
                a[i] = j
                v = a[0] + a[1] * 10 + a[2] * 100 + a[3] * 1000
                if v not in d:
                    np = v
                    break
                a[i] = orig
            if np != -1:
                break
        ans.append(np)
        d[p] -= 1
        d[np] = 1
    return (c, ans)


DEBUG = 'DEBUG' in os.environ


def inp():
    return sys.stdin.readline().rstrip()


def read_int():
    return int(inp())


def read_ints():
    return [int(e) for e in inp().split()]


def dprint(*value, sep=' ', end='\n'):
    if DEBUG:
        print(*value, sep=sep, end=end)


def __starting_point():
    main()


__starting_point()
