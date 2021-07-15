n, p, q, r = map(int, input().split())
a = [int(i) for i in input().split()]
min_suf = [0] * n
max_suf = [0] * n
min_suf[-1] = [n - 1, a[n - 1]]
max_suf[-1] = min_suf[-1]
pqr = [0] * n
qr = [0] * n
rr = [0] * n
rr[-1] = a[-1] * r
for i in range(n - 2, -1, -1):
    if a[i] < min_suf[i + 1][1]:
        min_suf[i] = [i, a[i]]
    else:
        min_suf[i] = min_suf[i + 1]
    if a[i] > max_suf[i + 1][1]:
        max_suf[i] = [i, a[i]]
    else:
        max_suf[i] = max_suf[i + 1]
    if r < 0:
        rr[i] = min_suf[i][1] * r
    else:
        rr[i] = max_suf[i][1] * r
for i in range(n):
    qr[i] = a[i] * q + rr[i]
for i in range(n - 2, -1, -1):
    qr[i] = max(qr[i], qr[i + 1])
ans = a[0] * p + qr[0]
for i in range(n):
    ans = max(a[i] * p + qr[i], ans)
print(ans)
