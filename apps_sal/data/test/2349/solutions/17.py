import sys
import os
3


def main():
    T = read_int()
    for _ in range(T):
        ans = solve(read_int())
        print(len(ans))
        print(*ans)


def solve(N):
    ans = [N]
    i = 2
    while i * (i - 1) <= N:
        v = N // i
        if ans[-1] != v:
            ans.append(v)
        i += 1

    v = ans[-1]
    for i in range(v - 1, -1, -1):
        ans.append(i)
    ans.reverse()
    return ans


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
