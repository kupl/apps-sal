def R(): return map(int, input().split())


n, M = R()
a = list(R())
a = [0] + a + [M]
b = [0] * (n + 2)
c = [0] * (n + 2)

for i in range(1, n + 2):
    if i % 2:
        b[i] = b[i - 1] + a[i] - a[i - 1]
        c[i] = c[i - 1]
    else:
        b[i] = b[i - 1]
        c[i] = c[i - 1] + a[i] - a[i - 1]

ans = b[n + 1]
for i in range(0, n + 1):
    if i % 2:
        k = a[i] + 1
        if k == a[i + 1]:
            continue
        t = b[i] + (c[n + 1] - c[i + 1]) + a[i + 1] - k
    else:
        k = a[i + 1] - 1
        if k == a[i]:
            continue
        t = b[i + 1] + (c[n + 1] - c[i]) - 1
    # dbvar(t)
    ans = max(ans, t)
print(ans)
