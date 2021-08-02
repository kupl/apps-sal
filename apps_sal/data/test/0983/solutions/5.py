n, p, q, r = list(map(int, input().split()))
a = list(map(int, input().split()))

pa = [p * a[0]] * n
for i in range(1, n):
    pa[i] = max(pa[i - 1], p * a[i])

qa = [q * a[0] + pa[0]] * n
for i in range(1, n):
    qa[i] = max(qa[i - 1], q * a[i] + pa[i])

ra = [r * a[0] + qa[0]] * n
for i in range(1, n):
    ra[i] = max(ra[i - 1], r * a[i] + qa[i])

print(max(ra))
