k, n = map(int, input().split())
a = list(map(int, input().split()))

m = 0
for i in range(n - 1):
    if a[i + 1] - a[i] > m:
        m = a[i + 1] - a[i]
if k - a[n - 1] + a[0] > m:
    m = k - a[n - 1] + a[0]
print(k - m)
