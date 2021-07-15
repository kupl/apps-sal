N, M, Q = map(int, input().split())
#N 500 に合わせて少し余分に準備
p = [[0] * 510 for i in range(510)]

for i in range(M):
  l, r = map(int, input().split())
  p[l][r] += 1
#print(p)
#print("")

#1 ~ N にすることで周囲に空白を用意
for i in range(1, N + 1):
  for j in range(1, N + 1):
    p[i][j] += p[i][j - 1]
#print(p)
#print("")

for i in range(1, N + 1):
  for j in range(1, N + 1):
    p[i][j] += p[i - 1][j ]    
#print(p)
#print("")

for i in range(Q):
  l, r = map(int, input().split())
  ans = p[r][r] + p[l - 1][l - 1] - p[r][l - 1] - p[l - 1][r]
  print(ans)
