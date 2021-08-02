N, K = list(map(int, input().split()))


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
    return binomial_coefficients


mod = 10**9 + 7
k = 2000
f = genCombinationFunction(k, mod)
for i in range(1, K + 1):
    redballs = N - K
    position = redballs + 1

    order = f(position, i)
    order *= f(K - 1, i - 1)
    print((order % mod))
