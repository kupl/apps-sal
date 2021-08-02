k, n = map(int, input().split())
a = [*map(int, input().split())]
d = [0] * n
for i in range(n - 1):
    d[i] = a[i + 1] - a[i]
d[-1] = a[0] + k - a[-1]
print(k - max(d))
