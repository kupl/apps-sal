#592_D

import sys

n = int(input())

vs = []

for i in range(0, 3):
    ln = [int(j) for j in sys.stdin.readline().rstrip().split(" ")]
    vs.append(ln)

vt = {}

f = True

for i in range(0, n - 1):
    edg = [int(j) for j in sys.stdin.readline().rstrip().split(" ")]
    if edg[0] in vt:
        vt[edg[0]].append(edg[1])
    else:
        vt[edg[0]] = [edg[1]]
    if edg[1] in vt:
        vt[edg[1]].append(edg[0])
    else:
        vt[edg[1]] = [edg[0]]

st = -1
for i in vt:
    if len(vt[i]) > 2:
        f = False
        break
    if len(vt[i]) == 1:
        st = i

if f:
    combos = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    m = -1
    ms = -1
    for i in range(0, len(combos)):
        cost = 0
        seq = [0] * (n)
        vert = st
        vis = {}
        for j in range(0, len(vs[0])):
            vis[vert] = True
            cost += vs[combos[i][j % 3] - 1][vert - 1]
            seq[vert - 1] = combos[i][j % 3]
            vert = vt[vert]
            if j == len(vs[0]) - 1:
                break
            if vert[0] in vis:
                vert = vert[1]
            else:
                vert = vert[0]
        if m == -1 or cost < m:
            m = cost
            ms = seq
    print(m)
    print(" ".join([str(i) for i in ms]))
else:
    print(-1)

