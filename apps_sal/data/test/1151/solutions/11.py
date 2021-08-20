from bisect import bisect_left as bi
(n, u) = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort()
c = []
for i in range(n - 1):
    b = bi(a, a[i] + u)
    if b != n:
        if a[b] == a[i] + u:
            b = b + 1
    b = a[b - 1]
    if b - a[i] != 0:
        c.append((b - a[i + 1]) / (b - a[i]))
if len(c) == 0 or max(c) == 0:
    print(-1)
else:
    print(max(c))
