import sys
sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    L = input()
    n = len(L)
    res = 0
    cnt = 0
    for i in range(n):
        if L[i] == '1':
            rest = n - (i + 1)
            res += pow(2, cnt, mod) * pow(3, rest, mod) % mod
            res %= mod
            cnt += 1
    res += pow(2, cnt, mod)
    print(res % mod)


def __starting_point():
    resolve()


__starting_point()
