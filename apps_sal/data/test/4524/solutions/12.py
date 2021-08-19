def modular_pow(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = result * base % modulus
        exponent = exponent >> 1
        base = base * base % modulus
    return result


(len_a, len_b) = list(map(int, input().split()))
a = input()[::-1]
b = input()[::-1]
dp = list(range(len_b))
dp[len(b) - 1] = 1
for i in range(len(b) - 2, -1, -1):
    dp[i] = dp[i + 1]
    if b[i] == '1':
        dp[i] += 1
primo = 998244353
soma = 0
for i in range(len_a - 1, -1, -1):
    if i < len(b) and a[i] == '1':
        partial = pow(2, i, primo)
        soma += partial * dp[i]
        soma = soma % primo
print(soma)
