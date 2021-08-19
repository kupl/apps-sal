(H, W, M) = map(int, input().split())
L = [[int(l) for l in input().split()] for _ in range(M)]
hlist = [0] * (H + 1)
wlist = [0] * (W + 1)
for l in L:
    hlist[l[0]] += 1
    wlist[l[1]] += 1
hmax = max(hlist)
wmax = max(wlist)
h = hlist.count(hmax)
w = wlist.count(wmax)
ans = hmax + wmax - 1
cnt = 0
for l in L:
    if hlist[l[0]] == hmax and wlist[l[1]] == wmax:
        cnt += 1
if cnt < h * w:
    ans += 1
print(ans)
