(n, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
d = 0
c = 0
t = 0
while t < k:
    if d == n:
        d += 1
        break
    c += a[d]
    g = min(8, c)
    t += g
    d += 1
    c = c - g
if d == n + 1:
    print(-1)
else:
    print(d)
