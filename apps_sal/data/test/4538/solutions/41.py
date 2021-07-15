import math
N, D = map(int, input().split())

ans = 0
for i in range(N):
  X, Y = map(int, input().split())
  dis = math.sqrt(X ** 2 + Y ** 2)
  if dis <= D:
    ans += 1

print(ans)
