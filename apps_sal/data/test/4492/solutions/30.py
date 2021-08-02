n, x = list(map(int, input().split()))
a = list(map(int, input().split()))
b = []
for i in range(1, n):
    b.append(a[i] + a[i - 1])
b.append(0)

res = 0
for i in range(n - 1):
    dif = max(b[i] - x, 0)
    minus = min(dif, a[i + 1])
    b[i + 1] -= minus
    b[i] -= dif
    res += dif

print(res)
