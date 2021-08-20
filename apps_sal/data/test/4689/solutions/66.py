(k, n) = map(int, input().split())
a = list(map(int, input().split()))
d = 0
for i in range(n - 1):
    d = max(a[i + 1] - a[i], d)
print(min(k - d, a[-1] - a[0]))
