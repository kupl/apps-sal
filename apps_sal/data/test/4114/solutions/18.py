# 初期入力
from collections import defaultdict
from bisect import bisect_right
import sys
input = sys.stdin.readline  # 文字列では使わない
N = int(input())
xyh = [0] * N
h_list = [0] * N

for i in range(N):
    x, y, h = (int(i) for i in input().split())
    xyh[i] = x, y, h
    h_list[i] = h

xyh.sort(key=lambda x: x[2])
h_list.sort()
ind = bisect_right(h_list, 0)
H = defaultdict(set)

for x, y, h in xyh[ind:]:
    for cx in range(101):
        for cy in range(101):
            xx = x - cx
            yy = y - cy
            if cx <= x and cy <= y:
                H[(cx, cy)].add((h + xx + yy))
            elif cx > x and cy <= y:
                H[(cx, cy)].add((h - xx + yy))
            elif cx <= x and cy > y:
                H[(cx, cy)].add((h + xx - yy))
            elif cx > x and cy > y:
                H[(cx, cy)].add((h - xx - yy))

# print(xyh)
#H.sort(key =lambda x:x[1])
if len(xyh[ind:]) == 1:
    print(*xyh[-1])
else:
    for k, v in H.items():

        if len(v) == 1:
            vv = v.pop()
            if 0 <= vv:
                print(*k, vv)
            elif vv < 0:
                print(*k, 0)
