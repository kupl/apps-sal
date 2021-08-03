H, W, M = list(map(int, input().split()))
hs = [0] * H
ws = [0] * W
s = set()

for i in range(M):
    r, c = list(map(int, input().split()))
    r -= 1
    c -= 1
    hs[r] += 1
    ws[c] += 1
    s.add((r, c))
mh = 0
mw = 0
for i in range(H):
    mh = max(mh, hs[i])
for j in range(W):
    mw = max(mw, ws[j])

i_s = list()
j_s = list()
for i in range(H):
    if mh == hs[i]:
        i_s.append(i)
for j in range(W):
    if mw == ws[j]:
        j_s.append(j)
ans = mh + mw
for i in i_s:
    for j in j_s:
        if (i, j) in s:
            continue
        print(ans)
        return
ans -= 1
print(ans)
