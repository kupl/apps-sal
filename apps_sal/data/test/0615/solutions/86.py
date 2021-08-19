(n, *a) = map(int, open(0).read().split())
for i in range(n - 1):
    a[i + 1] += a[i]
(j, k) = (0, 2)
m = 1e+18
for i in range(1, n - 1):
    while abs(a[j] * 2 - a[i]) > abs(a[j + 1] * 2 - a[i]):
        j += 1
    while abs(a[k] * 2 - a[i] - a[n - 1]) > abs(a[k + 1] * 2 - a[i] - a[n - 1]):
        k += 1
    t = (a[j], a[i] - a[j], a[k] - a[i], a[n - 1] - a[k])
    m = min(m, max(t) - min(t))
print(m)
