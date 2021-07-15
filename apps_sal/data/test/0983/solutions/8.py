n, p, q, r = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
crmx, crmn = [a[n - 1]] * n, [a[n - 1]] * n

for i in range(n - 2, -1, -1):
    crmx[i] = max(crmx[i + 1], a[i])
    crmn[i] = min(crmn[i + 1], a[i])

ans = 0 - 10 ** 21

mn, mx = a[0], a[0]

for i in range(n):
    cans = q * a[i]
    mx = max(mx, a[i])
    mn = min(mn, a[i])
    cans += max(mx * p, mn * p)
    cans += max(crmx[i] * r, crmn[i] * r)
    ans = max(ans, cans)

print(ans)

