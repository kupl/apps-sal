M = 10 ** 9 + 7
(k, n) = (int(input()), len(input()))
a = t = pow(26, k, M)
for i in range(1, k + 1):
    t = t * 25 * (i + n - 1) * pow(26 * i, -1, M) % M
    a += t
print(a % M)
