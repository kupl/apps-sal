(H, W, M) = map(int, input().split())
P = [list(map(int, input().split())) for i in range(M)]
for p in P:
    p[0] -= 1
    p[1] -= 1
cnth = [0] * H
cntw = [0] * W
ans = 0
for p in P:
    cnth[p[0]] += 1
for p in P:
    cntw[p[1]] += 1
mxh = max(cnth)
mxw = max(cntw)
cntx = 0
for p in P:
    if cnth[p[0]] == mxh and cntw[p[1]] == mxw:
        cntx += 1
if cntx == cnth.count(mxh) * cntw.count(mxw):
    ans = mxh + mxw - 1
else:
    ans = mxh + mxw
print(ans)
