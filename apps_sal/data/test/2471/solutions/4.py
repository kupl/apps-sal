import sys
import numpy as np


def sr(): return sys.stdin.readline().rstrip()
def ir(): return int(sr())
def lr(): return list(map(int, sr().split()))


H, W, N = lr()
shift = ((0, 0), (0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1))

l = []

for n in range(N):
    a, b = lr()
    for s in shift:
        aa = a + s[0] - 1
        bb = b + s[1] - 1
        if aa < 1 or aa > H - 2:
            continue
        if bb < 1 or bb > W - 2:
            continue
        l.append((aa - 1, bb - 1))
if len(l) == 0:
    print((H - 2) * (W - 2))
    [print(0) for _ in range(9)]
    return
l.sort()
m = {i: 0 for i in range(10)}
pre = l[0]
c = 1
for ll in l[1:]:
    if pre == ll:
        c += 1
    else:
        m[c] += 1
        pre = ll
        c = 1
m[c] += 1
m[0] = (H - 2) * (W - 2) - sum(m.values())
for v in m.values():
    print(v)
