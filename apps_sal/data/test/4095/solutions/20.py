n, m = map(int,input().split())
a = list(map(int,input().split()))
d = {}
d[0] = 1
has = False
sx = 0
ans = 0
for r in range(n):
    if a[r] < m:
        sx -= 1
    elif a[r] > m:
        sx += 1
    else:
        has = True
    if has:
        ans += d.get(sx,0) + d.get(sx-1,0)
    else:
        t = d.get(sx, 0) + 1
        d[sx] = t
print(ans)
