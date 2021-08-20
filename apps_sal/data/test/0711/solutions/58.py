import sys
sys.setrecursionlimit(10 ** 9)


def mi():
    return map(int, input().split())


def ii():
    return int(input())


def isp():
    return input().split()


def deb(text):
    print('-------\n{}\n-------'.format(text))


INF = 10 ** 20


class Counting:

    def __init__(self, maxim, mod):
        maxim += 1
        self.mod = mod
        self.fact = [0] * maxim
        self.fact[0] = 1
        for i in range(1, maxim):
            self.fact[i] = self.fact[i - 1] * i % mod
        self.invfact = [0] * maxim
        self.invfact[maxim - 1] = pow(self.fact[maxim - 1], mod - 2, mod)
        for i in reversed(range(maxim - 1)):
            self.invfact[i] = self.invfact[i + 1] * (i + 1) % mod

    def nCk(self, n, r):
        if n < 0 or n < r:
            return 0
        return self.fact[n] * self.invfact[r] * self.invfact[n - r] % self.mod

    def nPk(self, n, r):
        if n < 0 or n < r:
            return 0
        return self.fact[n] * self.invfact[n - r] % self.mod


def main():
    (N, M) = mi()
    MOD = 10 ** 9 + 7
    if N == 1:
        print(1)
        return

    def prime_factorize(n):
        P = []
        P_set = set()
        while n % 2 == 0:
            P.append(2)
            P_set.add(2)
            n //= 2
        f = 3
        while f * f <= n:
            if n % f == 0:
                P.append(f)
                P_set.add(f)
                n //= f
            else:
                f += 2
        if n != 1:
            P.append(n)
            P_set.add(n)
        P_count = {p: 0 for p in P_set}
        for p in P:
            P_count[p] += 1
        return P_count
    ans = 1
    counting = Counting(3 * 10 ** 5 + 10, MOD)
    for (p, e) in prime_factorize(M).items():
        ans *= counting.nCk(e + N - 1, e)
        ans %= MOD
    print(ans % MOD)


def __starting_point():
    main()


__starting_point()
