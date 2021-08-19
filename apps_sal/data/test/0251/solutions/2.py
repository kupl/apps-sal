(n, k) = list(map(int, input().split()))
h = list(map(int, input().split()))
hs = {}
mx = 0
mn = 10 ** 6
for a in h:
    mx = max(mx, a)
    mn = min(mn, a)
    if a not in hs:
        hs[a] = 0
    hs[a] += 1
ans = 0
cur = 0
curcl = 0
for i in range(mx, mn, -1):
    if i not in hs:
        nc = 0
    else:
        nc = hs[i]
    if cur + nc + curcl <= k:
        cur += nc + curcl
        curcl += nc
    else:
        ans += 1
        curcl += nc
        cur = curcl
if cur > 0:
    ans += 1
print(ans)
