k, n = map(int, input().split())
a = list(map(int, input().split()))
dd = k - a[-1] + a[0]
d = 0
for i in range(n - 1):
    d = max(d, a[i + 1] - a[i])
d = max(d, dd)
print(k - d)
