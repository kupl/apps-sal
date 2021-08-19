def mod_pow(a, n, mod):
    """
    二分累乗法による a^n (mod m)の実装
    :param a: 累乗の底
    :param n: 累乗の指数
    :param mod: 法
    :return: a^n (mod m)
    """
    result = 1
    a_n = a
    while n > 0:
        if n & 1:
            result = result * a_n % mod
        a_n = a_n * a_n % mod
        n >>= 1
    return result


class ModCombination:
    """
    nCk (mod m)を扱うクラス
    """

    def __init__(self, mod, n_max):
        """
        イニシャライザ
        予め 1~nの階乗と階乗の逆元を計算しておく
        :param mod: 法
        :param n_max: nの最大値(100,000で約1秒)
        """
        self.mod = mod
        self.n_max = n_max
        self.facts = [1, 1]
        self.inverses = [None, 1]
        self.fact_inverses = [1, 1]
        for i in range(2, self.n_max + 1):
            self.facts.append(self.facts[i - 1] * i % self.mod)
            self.inverses.append(self.mod - self.inverses[self.mod % i] * (self.mod // i) % self.mod)
            self.fact_inverses.append(self.fact_inverses[i - 1] * self.inverses[i] % self.mod)

    def mod_combination(self, n, k):
        """
        nCk (mod m)を計算する
        :param n: n
        :param k: k
        :return: nCk (mod m)
        """
        if k == 0:
            return 1
        if n == 0:
            return 0
        denominator = self.fact_inverses[k] * self.fact_inverses[n - k] % self.mod
        return self.facts[n] * denominator % self.mod


MOD = 998244353
(N, M, K) = list(map(int, input().split(' ')))
ans = 0
comb = ModCombination(mod=MOD, n_max=N)
for k in range(0, K + 1):
    ans += M * comb.mod_combination(N - 1, k) % MOD * mod_pow(M - 1, N - 1 - k, MOD)
    ans %= MOD
print(ans)
