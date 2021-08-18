import numpy as np
N, M, K = [int(_) for _ in input().split()]
mod = 998244353


class Factorial:
    def __init__(self, max_fact, mod):
        f = [1] * (max_fact + 1)
        for idx in range(2, max_fact + 1):
            f[idx] = f[idx - 1] * idx
            f[idx] %= mod
        if mod > max_fact:
            fi = [pow(f[-1], mod - 2, mod)]
            for idx in range(max_fact, 0, -1):
                fi += [fi[-1] * idx % mod]
            fi = fi[::-1]
        else:
            fi = [pow(n, mod - 2, mod) for n in f]
        self.mod = mod
        self.f = f
        self.fi = fi

    def factorial(self, n):
        return self.f[n]

    def factorial_inverse(self, n):
        return self.fi[n]

    def combination(self, n, r):
        f = self.f
        fi = self.fi
        return f[n] * fi[r] * fi[n - r] % self.mod

    def permutation(self, n, r):
        return self.f[n] * self.fi[n - r] % self.mod

    def homogeneous_product(self, n, r):
        f = self.f
        fi = self.fi
        return f[n + r - 1] * fi[r] * fi[n - 1] % self.mod


max_fact = N
fact_instance = Factorial(max_fact, mod)
comb = fact_instance.combination
ans = 0
for r in range(K + 1):
    ans += comb(N - 1, r) * M * pow(M - 1, N - r - 1, mod)
    ans %= mod
print(ans)
