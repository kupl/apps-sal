n, m = list(map(int, input().split()))
a = 5 * [n // 5]
for i in range(1, n % 5 + 1):
    a[i] += 1

b = 5 * [m // 5]
for i in range(1, m % 5 + 1):
    b[i] += 1

cnt = a[0] * b[0]
for i in range(1, 5):
    cnt += a[i] * b[5 - i]

print(cnt)
