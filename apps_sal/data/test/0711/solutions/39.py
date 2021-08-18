import sys
sys.setrecursionlimit(10 ** 8)
MOD = 10 ** 9 + 7
def Z(): return int(input())
def ZZ(): return [int(_) for _ in input().split()]


def main():
    N, M = ZZ()
    MAX_E = 50

    fact = [1] * (N + MAX_E + 1)
    ifact = [1] * (N + MAX_E + 1)

    for i in range(1, N + MAX_E + 1):
        fact[i] = i * fact[i - 1]
        fact[i] %= MOD
    ifact[N + MAX_E] = pow(fact[N + MAX_E], MOD - 2, MOD)
    for i in range(N + MAX_E)[::-1]:
        ifact[i] = ((i + 1) * ifact[i + 1]) % MOD

    def combination(n, r):
        if r < 0 or r > n:
            return 0
        return (fact[n] * ifact[n - r] * ifact[r]) % MOD

    def prime_factor(num):
        i = 2
        ret = []
        while i * i <= num:
            if num % i != 0:
                i += 1
                continue
            cc = 0
            while num % i == 0:
                num //= i
                cc += 1
            ret.append([i, cc])
            i += 1
        if num != 1:
            ret.append([num, 1])
        return ret

    ps = prime_factor(M)
    ans = 1
    for p, e in ps:
        ans *= combination(N + e - 1, N - 1)
        ans %= MOD
    print(ans)

    return


def __starting_point():
    main()


__starting_point()
