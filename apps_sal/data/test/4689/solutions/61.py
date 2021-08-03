k, n = map(int, input().split())
a = list(map(int, input().split()))

da = [-1] * n
da[n - 1] = k - a[n - 1] + a[0]
for i in range(n - 1):
    da[i] = a[i + 1] - a[i]
print(k - max(da))
