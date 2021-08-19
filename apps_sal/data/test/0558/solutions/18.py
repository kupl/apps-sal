n, m, k = list(map(int, input().split()))
MOD = 998244353


class Combination:
    def __init__(self, n, mod):
        self.n = n
        self.mod = mod

        self.f = self._get_f()
        self.fi = self._get_fi()

    def __call__(self, k):
        if not 0 <= k <= self.n:
            return 0
        else:
            num = self.f[self.n]
            deninv = (self.fi[k] * self.fi[self.n - k]) % self.mod
            return (num * deninv) % self.mod

    def _get_f(self):
        f = 1
        lf = [1]

        for i in range(1, self.n + 1):
            f = (f * i) % self.mod
            lf.append(f)

        return lf

    def _get_fi(self):
        ii = 1
        lii = [0, 1]  # [i^-1 modulo mod for i in 0, ..., n]
        fi = 1
        lfi = [1, 1]

        for i in range(2, self.n + 1):
            ii = (-lii[self.mod % i] * (self.mod // i)) % self.mod
            lii.append(ii)

            fi = (fi * ii) % self.mod
            lfi.append(fi)

        return lfi


c = Combination(n - 1, MOD)


def n_pattern(i):
    result = m
    result *= c(i)
    result %= MOD
    result *= pow(m - 1, n - i - 1, MOD)
    result %= MOD
    return result


answer = sum(n_pattern(i) for i in range(k + 1)) % MOD
print(answer)
