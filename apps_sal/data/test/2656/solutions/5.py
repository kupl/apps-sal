def f_strivore(MOD=10**9 + 7):
    K = int(input())
    S = input()
    length = len(S)

    class Combination(object):
        """素数 mod に対する二項係数の計算"""
        __slots__ = ['mod', 'fact', 'factinv']

        def __init__(self, max_val_arg: int = 10**6, mod: int = 10**9 + 7):
            fac, inv = [1], []
            fac_append, inv_append = fac.append, inv.append

            for i in range(1, max_val_arg + 1):
                fac_append(fac[-1] * i % mod)

            inv_append(pow(fac[-1], -1, mod))
            for i in range(max_val_arg, 0, -1):
                inv_append((inv[-1] * i) % mod)

            self.mod, self.fact, self.factinv = mod, fac, inv[::-1]

        def combination(self, n, r):
            return (0 if n < 0 or r < 0 or n < r
                    else self.fact[n] * self.factinv[r] * self.factinv[n - r] % self.mod)

    comb = Combination(length + K).combination
    f = [1] * (K + 1)
    tmp = 1
    for n in range(K + 1):
        f[n] = (comb(length + n - 1, length - 1) * tmp) % MOD
        tmp = (tmp * 25) % MOD
    g = [1] * (K + 1)
    for n in range(1, K + 1):
        g[n] = (f[n] + 26 * g[n - 1]) % MOD
    return g[K]


print(f_strivore())
