
import sys
from collections import Counter

H, W, M = map(int, sys.stdin.readline().rstrip().split())  # 行数H、列数W、爆弾数M
hcnt = [0] * H  # 何行目に何個あるか
wcnt = [0] * W  # 何列目に何個あるか
bomb = []

for i in range(M):
    bh, bw = map(int, sys.stdin.readline().rstrip().split())
    hcnt[bh - 1] += 1  # 行方向
    wcnt[bw - 1] += 1  # 列方向
    bomb.append((bh - 1, bw - 1))
#hcnt [2,1]
# wcnt[1,1,1]
# bomb[[1,1],[0,0],[0,2]]
hmax = max(hcnt)  # 2
wmax = max(wcnt)  # 1

crs = 0  # hmax and wmax crosspoint
for (i, j) in bomb:
    if hcnt[i] == hmax and wcnt[j] == wmax:
        crs += 1
# all crosspoint has bomb
if crs == Counter(hcnt)[hmax] * Counter(wcnt)[wmax]:
    print(hmax + wmax - 1)
# more than one crosspoint has no bomb
else:
    print(hmax + wmax)
