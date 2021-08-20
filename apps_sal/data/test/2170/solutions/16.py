max_fact = 5 * 10 ** 5
mod = 10 ** 9 + 7
f = [1] * (max_fact + 1)
for idx in range(2, max_fact + 1):
    f[idx] = f[idx - 1] * idx
    f[idx] %= mod
fi = [pow(f[-1], mod - 2, mod)]
for idx in range(max_fact, 0, -1):
    fi += [fi[-1] * idx % mod]
fi = fi[::-1]


def factorial(n):
    return f[n]


def factorial_inverse(n):
    return fi[n]


def combination(n, r):
    return f[n] * fi[r] * fi[n - r] % mod


def permutation(n, r):
    return f[n] * fi[n - r] % mod


def homogeneous_product(n, r):
    return f[n + r - 1] * fi[r] * fi[n - 1] % mod


comb = combination
perm = permutation
(N, M) = [int(_) for _ in input().split()]
ans = 0
for p in range(N + 1):
    ans += (-1) ** p * comb(N, p) * perm(M - p, N - p)
    ans %= mod
ans *= perm(M, N)
ans %= mod
print(ans)
