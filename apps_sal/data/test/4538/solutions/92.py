import math

N, D = map(int, input().split())
ans = 0

for i in range(N):
  x, y = map(int, input().split())
  ans += 1 if math.sqrt(x**2 + y**2) <= D else 0

print(ans)
