import math

def __starting_point():
  n, r = [int(x) for x in input().split()]
  x = [int(x) for x in input().split()]
  h = [None] * n
  for i in range(n):
    h[i] = r
    for j in range(i):
      if abs(x[i] - x[j]) <= 2 * r:
        h[i] = max(h[i], h[j] + math.sqrt(math.pow(2 * r, 2) - math.pow(x[i] - x[j], 2)))
  print(*h)

__starting_point()
