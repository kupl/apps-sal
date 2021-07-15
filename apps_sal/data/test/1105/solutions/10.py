import sys
from collections import defaultdict

n = int(sys.stdin.readline())
d = defaultdict(lambda:-1)
for i in range(0, n):
  x, k = map(int, sys.stdin.readline().split())
  z = d[k]
  if x == z + 1:
    d[k] = x
  elif x > z + 1:
    print('NO')
    return

print('YES')
