import math

N, D = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(N):
  for j in range(i+1, N):
    dis = 0
    for d in range(D):
      dis += (X[i][d] - X[j][d])**2
    dis = math.sqrt(dis)
    ans += dis.is_integer()

print(ans)
