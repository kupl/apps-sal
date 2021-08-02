H, W, M = map(int, input().split())
l = [list(map(int, input().split(" "))) for i in range(M)]
h = [0] * H
w = [0] * W
for i in range(M):
    h[l[i][0] - 1] += 1
    w[l[i][1] - 1] += 1
maxh = max(h)
maxw = max(w)
hlist = []
wlist = []
for i in range(H):
    if h[i] == maxh:
        hlist.append(i)
for i in range(W):
    if w[i] == maxw:
        wlist.append(i)
c = 0
for i in range(M):
    if h[l[i][0] - 1] == maxh and w[l[i][1] - 1] == maxw:
        c += 1
if len(hlist) * len(wlist) == c:
    print(maxh + maxw - 1)
else:
    print(maxh + maxw)
