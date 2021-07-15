import sys
readline = sys.stdin.readline

N,C = map(int,readline().split())
sushi = [list(map(int,readline().split())) for i in range(N)]
import copy
revsushi = copy.deepcopy(sushi)[::-1]
for i in range(len(sushi)-1, 0, -1):
  sushi[i][0] = sushi[i][0] - sushi[i - 1][0]

for i in range(len(revsushi)):
  revsushi[i][0] = C - revsushi[i][0]
for i in range(len(revsushi)-1, 0, -1):
  revsushi[i][0] = revsushi[i][0] - revsushi[i - 1][0]

# 左回り/右回りにi個食べたときの結果
# 0個のときは0を入れておく
left = [[0] * 2 for i in range(N + 1)]
right = [[0] * 2 for i in range(N + 1)]

left[0] = [0,0]
right[0] = [0,0]

# 累積ポイント, そこまでのベストポイント
for i in range(len(sushi)):
  x,v = sushi[i]
  left[i + 1][0] = left[i][0] + v - x # 摂取カロリー - 消費カロリー
  if left[i + 1][0] > left[i][1]: # 前回までのベストより優れている
    left[i + 1][1] = left[i + 1][0]
  else:
    left[i + 1][1] = left[i][1]
    
# この状態で右回りにチェックしていく
best = left[-1][1] # 左回りにすべて取った場合を最大値としてスタート
cal = 0
for i in range(len(revsushi)):
  count = i + 1 # 取る寿司の数
  lp = left[N - count][1]
  # 逆回りに取れる寿司の最大値
  x,v = revsushi[i]
  cal += (v - x * 2)
  if lp + cal > best:
    best = lp + cal

# 右回りを作る
for i in range(len(revsushi)):
  x,v = revsushi[i]
  right[i + 1][0] = right[i][0] + v - x
  if right[i + 1][0] > right[i][1]:
    right[i + 1][1] = right[i + 1][0]
  else:
    right[i + 1][1] = right[i][1]

best = max(best, right[-1][1])
cal = 0
for i in range(len(sushi)):
  count = i + 1 # 取る寿司の数
  rp = right[N - count][1]
  # 逆回りに取れる寿司の最大値
  x,v = sushi[i]
  cal += (v - x * 2)
  if rp + cal > best:
    best = rp + cal

print(best)
