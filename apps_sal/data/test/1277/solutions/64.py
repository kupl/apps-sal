import sys
readline = sys.stdin.readline

# 青木君からの到達距離 - 高橋君からの到達距離が最も大きい場所に逃げるべき
# そこに到達したときに、
# 高橋君と青木君の距離が偶数のとき
# 青 - x - x - x - 高
# 青 - x - x - 高 - x
# x - 青 - x - 高 - x
# x - 青 - x - x - 高
# x - x - 青 - x - 高
# x - x - 青- 高 - x 
# x - x - x - 終 - x 
# 青木君からの距離 - 1が答え
# 高橋君と青木君の距離が奇数のとき
# 青 - x - x - 高
# 青 - x - 高 - x
# x - 青 - 高 - x
# x - 青 - x - 高
# x - x - 青 - 高
# x - x - 終 - x
# やっぱり青木君からの距離 - 1が答え
# つまり、
# ・[青木君からの距離が遠い場所について]
# ・[青木君からの距離 - 1]が答え

N,u,v = list(map(int,readline().split()))
G = [[] for i in range(N)]
for i in range(N - 1):
  a,b = list(map(int,readline().split()))
  G[a - 1].append(b - 1)
  G[b - 1].append(a - 1)

dist_from_u = [0 for i in range(N)] # 高橋君からの距離
dist_from_v = [0 for i in range(N)] # 青木君からの距離

stack = []
# 頂点, 高橋君からの距離, 親
stack.append([u - 1,0,-1])
while stack:
  e, dist, parent = stack.pop()
  dist_from_u[e] = dist
  for child in G[e]:
    if child == parent:
      continue
    stack.append([child, dist + 1, e])

stack = []
# 頂点, 青木君からの距離, 親
stack.append([v - 1,0,-1])
while stack:
  e, dist, parent = stack.pop()
  dist_from_v[e] = dist
  for child in G[e]:
    if child == parent:
      continue
    stack.append([child, dist + 1, e])
    
maxdiff_from_v = 0
for i in range(N):
  if dist_from_u[i] < dist_from_v[i]:
    if maxdiff_from_v < dist_from_v[i]:
      maxdiff_from_v = dist_from_v[i]
    
print((maxdiff_from_v - 1))

