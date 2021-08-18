n, d = map(int, input().split())
a = list(map(int, input().split()))
pref = [0 for i in range(n)]
c = 0
for i in range(n):
    c += a[i]
    if a[i] == 0:
        c = max(0, c)
    pref[i] = c
suff = [0 for i in range(n)]
suff[-1] = pref[-1]
mc = suff[-1]
for i in range(n - 2, -1, -1):
    suff[i] = max(mc, pref[i])
    mc = suff[i]
    if a[i] == 0 and i > 0:
        mc = pref[i - 1]
if max(suff) > d:
    print(-1)
    return
c = 0
ans = 0
for i in range(n):
    if a[i] != 0:
        c += a[i]
    else:
        if c < 0:
            ans += 1
            c = max(0, c)
            c += d - suff[i]
print(ans)
