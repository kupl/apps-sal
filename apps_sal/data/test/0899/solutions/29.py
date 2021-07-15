import sys

N, M = map(int, input().split())

memo = [[sys.maxsize]*(N+1) for _ in range(N+1)]
for i in range(1,N+1):
  memo[i][i] = 0

lst = []
for _ in range(M):
  a,b,c = map(int, input().split())
  memo[a][b] = c
  memo[b][a] = c
  lst.append((a,b,c))
  
for k in range(1,N+1):
  for i in range(1,N+1):
    for j in range(1,N+1):
      memo[i][j] = min(memo[i][j], memo[i][k] + memo[k][j])
      
cnt = 0
for a,b,c in lst:
  if memo[a][b] < c:
    cnt += 1
    
print(cnt)
