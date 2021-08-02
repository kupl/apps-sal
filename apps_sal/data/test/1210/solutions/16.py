n, p = [int(i) for i in input().split()]
b = []
for i in range(n):
    a = [int(i) for i in input().split()]
    if a[0] % p == 0:
        l = a[0] // p
    else:
        l = a[0] // p + 1
    r = a[1] // p
    s = max(0, r - l + 1)
    s /= a[1] - a[0] + 1
    b += [s]
res = 0
for i in range(-1, n - 1):
    res += (b[i] + b[i + 1] - b[i] * b[i + 1]) * 2000
print(res)
