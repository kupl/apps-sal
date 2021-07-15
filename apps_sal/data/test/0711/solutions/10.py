def prime_factorization(n):
    """
    nを素因数分解
    :param n:
    :return:素因数分解結果 [(素数S1, count S1),(素数S2, count S2), ...]

    """
    from math import sqrt
    if (n == 0): return []
    if (n == 1): return [(1, 1)]

    res = []
    for i in range(2, int(sqrt(n)) + 1):
        if n == 1: break
        cnt = 0
        while n % i == 0:
            cnt += 1
            n = n // i
        if cnt > 0:
            res.append((i, cnt))
    if n > 1:
        res.append((n, 1))

    return res


class ModFactorial:
    """
    階乗, 組み合わせ, 順列の計算
    """

    def __init__(self, n, MOD=10 ** 9 + 7):
        """

        :param n: 最大の要素数.
        :param MOD:
        """
        kaijo = [0] * (n + 10)
        gyaku = [0] * (n + 10)

        kaijo[0] = 1
        kaijo[1] = 1
        for i in range(2, len(kaijo)):
            kaijo[i] = (i * kaijo[i - 1]) % MOD
        gyaku[0] = 1
        gyaku[1] = 1
        for i in range(2, len(gyaku)):
            gyaku[i] = pow(kaijo[i], MOD - 2, MOD)
        self.kaijo = kaijo
        self.gyaku = gyaku
        self.MOD = MOD

    def nCm(self, n, m):
        return (self.kaijo[n] * self.gyaku[n - m] * self.gyaku[m]) % self.MOD

    def nPm(self, n, m):
        return (self.kaijo[n] * self.gyaku[n - m]) % self.MOD

    def factorial(self, n):
        return self.kaijo[n]


N, M = [int(_) for _ in input().split()]
if M == 1:
    print((1))
    return

primes = [v for _, v in prime_factorization(M)]

MOD = 10 ** 9 + 7
mf = ModFactorial(max(primes) + 1 + N, MOD)

ans = 1
for cnt in primes:
    ans = ans * mf.nCm(cnt + N - 1, N - 1)
    ans = ans % MOD
print(ans)

