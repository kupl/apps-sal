n, d = list(map(int, input().split()))
a = [0] + list(map(int, input().split()))
b = [0] * (n + 2)
b[n] = a[n]
now = a[n]
for i in range(n - 1, 0, -1):
    now = a[i] + max(now, 0)
    b[i] = now
now = 0
res = 0
for i in range(1, n + 1):
    if a[i] == 0:
        if now < 0:
            res += 1
            now = min(d, max(0, d - b[i + 1]))
    else:
        now += a[i]
        if now > d:
            res = -1
            break
print(res)
