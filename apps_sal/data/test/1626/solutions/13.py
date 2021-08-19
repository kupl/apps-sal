(n, k) = list(map(int, input().split()))
ara = list(map(int, input().split()))
arb = list(map(int, input().split()))
sum1 = 1
p_k = 10 ** k
p_k1 = 10 ** (k - 1)
p_k2 = 10 ** (k - 2)
M = 10 ** 9 + 7
for i in range(n // k):
    k = 0
    if p_k % ara[i] == 0:
        k = -1
    if (arb[i] + 1) * p_k1 % ara[i] == 0:
        k = k + 1
    if arb[i] * p_k1 % ara[i] == 0:
        k = k - 1
    sum1 *= p_k // ara[i] - p_k1 * (arb[i] + 1) // ara[i] + p_k1 * arb[i] // ara[i] + k + 1
    sum1 = sum1 % M
print(sum1 % (10 ** 9 + 7))
