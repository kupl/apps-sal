def MIS(): return map(int, input().split())


n, m = MIS()
a = [0] + list(MIS()) + [m]
inter = []
for i in range(n + 1):
    inter.append(a[i + 1] - a[i])
S = sum(inter[::2])

opt = S
cur = S
mul = 1 if n % 2 == 1 else -1
x = m
for i in range(n, 0, -1):
    if a[i] + 1 != a[i + 1]:
        cur += (x - a[i] - 1) * mul
        opt = max(opt, cur)
        x = a[i] + 1
    cur += (x - a[i]) * mul
    x = a[i]
    mul *= -1
    if a[i] - 1 != a[i - 1]:
        cur += mul
        opt = max(opt, cur)
        x -= 1
print(opt)
