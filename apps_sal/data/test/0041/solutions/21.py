n = int(input())
a = list(map(int, input().split()))
l, r, ll, rr, c = [0] * n, [0] * n, -10**9, 10**9, []
for i in range(n):
    if not a[i]: ll = i
    l[i] = i - ll
for i in range(n - 1, -1, -1):
    if not a[i]: rr = i
    r[i] = rr - i
for i in range(n): c.append(str(min(l[i], r[i])))
print(' '.join(c))
