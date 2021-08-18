H, W, M = map(int, input().split())

hs = [0] * H
ws = [0] * W
s = set()

for i in range(M):
    h, w = map(int, input().split())
    h -= 1
    w -= 1
    hs[h] += 1
    ws[w] += 1
    s.add((h, w))

mh = 0
mw = 0
for i in range(H):
    mh = max(mh, hs[i])
for j in range(W):
    mw = max(mw, ws[j])

l_s = list()
j_s = list()
for i in range(H):
    if mh == hs[i]:
        l_s.append(i)
for j in range(W):
    if mw == ws[j]:
        j_s.append(j)

ans = mh + mw
for i in l_s:
    for j in j_s:
        if (i, j) in s:
            continue
        print(ans)
        return
ans -= 1
print(ans)
