(N, K) = list(map(int, input().split()))
A = sorted(list(map(int, input().split())))
MOD = 10 ** 9 + 7
factorial = [1, 1]
inverse = [1, 1]
invere_base = [0, 1]
for i in range(2, N + 2):
    factorial.append(factorial[-1] * i % MOD)
    invere_base.append(-invere_base[MOD % i] * (MOD // i) % MOD)
    inverse.append(inverse[-1] * invere_base[-1] % MOD)


def nCr(n, r):
    if not 0 <= r <= n:
        return 0
    return factorial[n] * inverse[r] * inverse[n - r] % MOD


(MAX, MIN) = (0, 0)
for (i, a) in enumerate(A):
    MAX += a * nCr(i, K - 1)
    MIN += a * nCr(N - i - 1, K - 1)
    MAX %= MOD
    MIN %= MOD
print((MAX - MIN) % MOD)
