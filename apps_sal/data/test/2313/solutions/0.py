import sys
sys.setrecursionlimit(10 ** 5)


def int1(x):
    return int(x) - 1


def p2D(x):
    return print(*x, sep='\n')


def II():
    return int(sys.stdin.readline())


def MI():
    return map(int, sys.stdin.readline().split())


def LI():
    return list(map(int, sys.stdin.readline().split()))


def LLI(rows_number):
    return [LI() for _ in range(rows_number)]


def SI():
    return sys.stdin.readline()[:-1]


def solve():
    cs = [aa[0]]
    for a in aa[1:]:
        cs.append((cs[-1] + a) % md)
    inv = pow(n, md - 2, md)
    ans = []
    for k in range(1, n):
        cur = 0
        for i in range(1, n):
            if n - 1 - k * i < 0:
                break
            cur = (cur + cs[n - 1 - k * i]) % md
        cur = cur * inv % md
        ans.append(cur)
    ans.append(0)
    print(*ans)


md = 998244353
n = II()
aa = LI()
aa.sort()
solve()
