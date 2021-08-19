M = 10 ** 9 + 7
(n, k) = map(int, input().split())
a = c = 1
for i in range(1, min(n, k + 1)):
    m = n - i
    c = c * -~m * m * pow(i, M - 2, M) ** 2 % M
    a += c
print(a % M)
