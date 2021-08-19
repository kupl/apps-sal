(n, x, *a) = map(int, open((c := 0)).read().split())
for i in range(n - 1):
    s = max(a[i] + a[i + 1] - x, 0)
    a[i + 1] -= s
    if a[i + 1] < 0:
        a[i] += a[i + 1]
        a[i + 1] = 0
    c += s
print(c)
