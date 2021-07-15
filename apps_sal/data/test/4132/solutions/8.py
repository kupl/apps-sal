import math
N = int(input())
A = list(map(int, input().split()))

g = A[0]
for i in range(1, N):
  g = math.gcd(g, A[i])

print(g)
