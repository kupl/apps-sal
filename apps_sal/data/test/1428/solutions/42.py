#計算量 max(N ** 2, C ** 3)
N, C = list(map(int, input().split()))
D = [0] * C
for i in range(C):
  D[i] = list(map(int, input().split()))
grid = [0] * N
for i in range(N):
  grid[i] = list(map(int, input().split()))
  
#print(D, grid) 
grid3 = [[0] * C for i in range(3)]
#grid[i][j]:3で割って余りが i のマスで、色がjであるマスの個数
for i in range(N):
  for j in range(N):
    nn = (i + j) % 3
    color = grid[i][j] - 1
    grid3[nn][color] += 1
#print(grid3)  

score = [[0] * C for i in range(3)]
#score[i][j]:3で割って余りが i のマスを、色jにするときの違和感
#3 * C * C
for j in range(C):
  for i in range(3):
    for k in range(C): 
      score[i][j] += grid3[i][k] * D[k][j]
#print(score)            
ans = 10 ** 10  
for i in range(C):
  for j in range(C):
    if i != j:
      for k in range(C):
        if (i != k) and (j != k):
          now = score[0][i] + score[1][j] + score[2][k]
          ans = min(ans, now)
print(ans)      




