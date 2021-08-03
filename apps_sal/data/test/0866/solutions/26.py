X, Y = map(int, input().split())

total = (X + Y) / 3
k = (2 * X - Y) // 3

if (total == int(total)) and (k >= 0):
    total = (X + Y) // 3

    mod = 10 ** 9 + 7

    modinv_table = [-1] * (k + 1)
    for i in range(1, k + 1):
        modinv_table[i] = pow(i, -1, mod)

    def binomial_coefficients(n, k):
        ans = 1
        for i in range(k):
            ans *= n - i
            ans *= modinv_table[i + 1]
            ans %= mod
        return ans

    print(binomial_coefficients(total, k))
else:
    print(0)
