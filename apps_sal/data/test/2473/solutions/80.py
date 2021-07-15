import sys
import itertools

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

N, K = lr()
XY = [lr() for _ in range(N)]
XY.sort()
answer = float('inf')
# 端の4点、まずはx軸の2点を選ぶ
for left,right in itertools.combinations(range(N),2):
  width = XY[right][0] - XY[left][0]
  pts = sorted(XY[left:right+1], key = lambda xy: xy[1])
  for D in range(len(pts)):
    if D + K - 1 >= len(pts):
      break
    y_max = pts[D+K-1][1]
    y_min = pts[D][1]
    area = (y_max - y_min) * width
    if area < answer:
      answer = area
    
print(answer)
