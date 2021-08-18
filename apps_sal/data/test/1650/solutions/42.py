import sys

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def modpow(a, n, mod):
    res = 1
    while n > 0:
        if n & 1:
            res = res * a % mod
        a = a * a % mod
        n >>= 1
    return res


def main():
    L = input()
    N = len(L)
    dp_1 = [0] * N
    dp_2 = [0] * N

    dp_1[0] = 1
    dp_2[0] = 2

    for i in range(1, N):
        if L[i] == "1":
            dp_2[i] = dp_2[i - 1] * 2

            dp_1[i] = dp_2[i - 1] + dp_1[i - 1] * 3

            dp_2[i] %= MOD
            dp_1[i] %= MOD
        else:
            dp_2[i] = dp_2[i - 1]

            dp_1[i] = dp_1[i - 1] * 3

            dp_2[i] %= MOD
            dp_1[i] %= MOD

    ans = dp_1[-1] + dp_2[-1]
    ans %= MOD
    print(ans)


def __starting_point():
    main()


__starting_point()
