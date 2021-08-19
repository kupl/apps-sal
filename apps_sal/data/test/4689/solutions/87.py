(k, n) = map(int, input().split())
(a, c) = ([*map(int, input().split())], [0] * n)
for i in range(n - 1):
    c[i] = a[i + 1] - a[i]
c[-1] = a[0] + k - a[-1]
print(k - max(c))
