import sys
from collections import defaultdict
readline = sys.stdin.readline
N = int(readline())
XYZ = [tuple(map(int, readline().split())) for _ in range(N)]
XYZI = [(x, y, z, i) for (i, (x, y, z)) in enumerate(XYZ, 1)]
XYZI.sort()
(X, Y, Z, IDX) = map(list, zip(*XYZI))
Di = defaultdict(list)
for i in range(N):
    (x, y, z, idx) = (X[i], Y[i], Z[i], IDX[i])
    Di[x].append((y, z, idx))
Ans = []
Ama = []
for L in Di.values():
    D2 = defaultdict(int)
    for (y, _, _) in L:
        D2[y] += 1
    pre = None
    st = None
    for (y, z, i) in L:
        if st is None and D2[y] == 1:
            if pre is not None:
                Ans.append((pre, i))
                pre = None
            else:
                pre = i
        elif st is not None:
            Ans.append((st, i))
            st = None
        else:
            st = i
        D2[y] -= 1
    if st:
        Ama.append(st)
    if pre:
        Ama.append(pre)
Le = len(Ama)
for i in range(Le // 2):
    Ans.append((Ama[2 * i], Ama[2 * i + 1]))
for a in Ans:
    sys.stdout.write('{} {}\n'.format(*a))
