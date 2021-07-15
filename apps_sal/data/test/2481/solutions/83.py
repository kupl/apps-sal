import sys
readline = sys.stdin.readline

H,W = map(int,readline().split())
C = [None] * 10
for i in range(10):
  C[i] = list(map(int,readline().split()))

for k in range(10):
  for i in range(10):
    for j in range(10):
      C[i][j] = min(C[i][j], C[i][k] + C[k][j])
      
ans = 0
for i in range(H):
  line = list(map(int,readline().split()))
  for j in range(len(line)):
    if line[j] == -1:
      continue
    ans += C[line[j]][1]
    
print(ans)
