(N, K) = [int(n) for n in input().split()]
NUM = 1000000007


def modpow(a, b):
    ans = 1
    while b != 0:
        if b % 2 == 1:
            ans *= a
            ans %= NUM
        a = a * a
        a %= NUM
        b //= 2
    return ans


C = [0 for _ in range(K + 1)]
for d in range(K):
    k = K - d
    L = K // k
    C[k] = modpow(L, N)
    for l in range(2, L + 1):
        C[k] -= C[l * k]
        if C[k] < 0:
            C[k] += NUM
        C[k] %= NUM
ans = 0
for k in range(1, K + 1):
    ans += k * C[k]
    ans %= NUM
print(ans)
