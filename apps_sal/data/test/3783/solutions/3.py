n, k = map(int, input().split())
m = 0x3b9aca07
r = 0
p = pow(2, n, m)
a = [1] + [0] * k
for i in range(k):
    for j in range(i, -1, -1):
        a[j + 1] += a[j]
        a[j] = a[j] * j % m
for i in range(k + 1):
    r += p * a[i]
    p = p * 500000004 * (n - i) % m
print(r % m)
