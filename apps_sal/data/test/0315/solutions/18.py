n, k = map(int, input().split())
a = list(map(int, input().split()))
c = 0
for i in range(n - 1):
    if a[i] + a[i + 1] < k:
        c += k - a[i] - a[i + 1]
        a[i + 1] += k - a[i] - a[i + 1]
print(c)
for i in range(n):
    print(a[i], end=' ')
