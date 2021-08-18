N, M, K = map(int, input().split())
mod = 998244353


def genCombinationFunction(max_k, mod):
    modinv_table = [-1] * (max_k + 1)
    modinv_table[1] = 1
    for i in range(2, max_k + 1):
        modinv_table[i] = (-modinv_table[mod % i] * (mod // i)) % mod

    def binomial_coefficients(n, k):
        ans = 1
        for i in range(k):
            ans *= n - i
            ans *= modinv_table[i + 1]
            ans %= mod
        return ans
    return binomial_coefficients, modinv_table


f, table = genCombinationFunction(10**6, mod)

ans = 0
C = 1
for i in range(K + 1):
    base = M * pow(M - 1, N - i - 1, mod)
    if i:
        C *= N - i
        C *= table[i]
        C %= mod
    ans += C * base
    ans %= mod
print(ans)
