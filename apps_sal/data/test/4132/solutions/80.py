import math
N = int(input())
A = list(map(int, input().split()))

# 攻撃：最大公約数を求める操作
g = A[0]
for i in range(1, N):
  g = math.gcd(g, A[i])

print(g)
