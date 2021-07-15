from heapq import heapify,heappush,heappop

N, M, S = map(int, input().split())

# !!グラフの作成!! #
tmp = [list(map(int, input().split())) for _ in range(M)]

U = [0 for _ in range(M)]
V = [0 for _ in range(M)]
A = [0 for _ in range(M)]
B = [0 for _ in range(M)]

for i in range(M):
  U[i] = tmp[i][0] -1
  V[i] = tmp[i][1] -1
  A[i] = tmp[i][2]
  B[i] = tmp[i][3]
A_m = max(A)
S = min(N*A_m, S)
#print(A_m)

I = [[] for _ in range(N * (N*A_m+1))] 
# 隣接リスト(頂点iで銀貨j枚持ちのとき、i*N*(A_m+1)+jとおく)
for i in range(M):
  for j in range(A[i], N*A_m+1):
    I[U[i]*(N*A_m+1)+j].append((V[i]*(N*A_m+1)+j-A[i],B[i]))
    I[V[i]*(N*A_m+1)+j].append((U[i]*(N*A_m+1)+j-A[i],B[i]))

for i in range(N):
  C, D = map(int, input().split())
  for j in range(N*A_m+1):
    I[i*(N*A_m+1)+j].append((i*(N*A_m+1)+min(C+j,N*A_m),D))
#print(I)

def dijkstra(I):# I:隣接リスト(頂点、コスト、そのほか制約) 
  N = len(I)
  task = [] 
  visited = [0 for _ in range(N)]
  min_cost = [0 for _ in range(N)]
  cost = [10**20 for _ in range(N)]
  prev_points = [0 for _ in range(N)]
  heappush(task, (0, S, -1))
  # !!比較値がスカラーでないときは、一番左の0を適宜変更する!! #
  # !!最初の点番号が0でないときは、真ん中の0を変更する!! #
  
  flag = 0
  while task:
    while task:
      c, p, prev = heappop(task)    
      if visited[p] == 0:
        break  
      if len(task) == 0:
        flag = 1
    if flag == 1:
      break
    #print(task)
    visited[p] = 1
    min_cost[p] = c
    prev_points[p] = prev
  
    for j, c_ad in I[p]: #制約が入るときはここに追加
      if visited[j] == 1: continue
      #print(p//(N*A_m+1),p%(N*A_m+1),j//(N*A_m+1),j%(N*A_m+1),c_ad)
      cost_next = next_cost(I, p, j, c, c_ad)
      if cost[j] > cost_next:
        cost[j] = cost_next
        heappush(task, (cost_next, j, p))

  return (min_cost, prev_points)

def next_cost(I, p, j, c, c_ad): # !!現在の点pから次の点jへのコストを計算する方法を記入!! #  
#c:点pにつくまでに払ったコスト、c_ad:次回追加されるコスト#
  return c + c_ad

min_cost, prev_points = dijkstra(I)

for i in range(1, N):
  print(min(min_cost[i*(N*A_m+1):(i+1)*(N*A_m+1)]))
