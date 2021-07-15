import math

def comb(n, r):
  if n <= 1:
    return 0
  return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

N, M = list(map(int, input().split()))
print(comb(N+M, 2) - N*M )
