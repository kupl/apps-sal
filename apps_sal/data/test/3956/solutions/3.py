import sys
sys.setrecursionlimit(10 ** 6)


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


def nCr(com_n, com_r):
    if com_n < com_r:
        return 0
    return fac[com_n] * ifac[com_r] % md * ifac[com_n - com_r] % md


def nHr(hn, hr):
    return nCr(hn + hr - 1, hr)


md = 998244353
n_max = 5000
fac = [1]
for i in range(1, n_max + 1):
    fac.append(fac[-1] * i % md)
ifac = [1] * (n_max + 1)
ifac[n_max] = pow(fac[n_max], md - 2, md)
for i in range(n_max - 1, 1, -1):
    ifac[i] = ifac[i + 1] * (i + 1) % md


def solve():
    res = 0
    for p in range(min(t, n) // 2 + 1):
        cur = nCr(t // 2, p) * nHr(k, n - 2 * p)
        if p & 1:
            res -= cur
        else:
            res += cur
        res %= md
    return res


(k, n) = MI()
ans = []
for t in range(2, k + 2):
    a = solve()
    ans.append(a)
    print(a)
ans.reverse()
for a in ans[1:]:
    print(a)
