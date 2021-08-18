
import sys
from collections import Counter

H, W, M = map(int, sys.stdin.readline().rstrip().split())
hcnt = [0] * H
wcnt = [0] * W
bomb = []

for i in range(M):
    bh, bw = map(int, sys.stdin.readline().rstrip().split())
    hcnt[bh - 1] += 1
    wcnt[bw - 1] += 1
    bomb.append((bh - 1, bw - 1))
hmax = max(hcnt)
wmax = max(wcnt)

crs = 0
for (i, j) in bomb:
    if hcnt[i] == hmax and wcnt[j] == wmax:
        crs += 1
if crs == Counter(hcnt)[hmax] * Counter(wcnt)[wmax]:
    print(hmax + wmax - 1)
else:
    print(hmax + wmax)
