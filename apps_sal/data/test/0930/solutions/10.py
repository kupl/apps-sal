class Factorial:
    def __init__(self, max_fact, mod):
        # mod should be prime number
        # using homogeneous_product(n,r), max_fact ≧ max(n+r-1)
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


max_fact = 4 * 10**5 + 100
mod = 10**9 + 7
fact_instance = Factorial(max_fact, mod)
comb_repl = fact_instance.homogeneous_product
comb = fact_instance.combination

N, K = [int(_) for _ in input().split()]
ans = 0
for r in range(min(N - 1, K) + 1):
    ans += comb(N, r) * comb_repl(N - r, r)
    ans %= mod
print(ans)
