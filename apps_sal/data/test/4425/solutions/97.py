from math import *

n, k = map(int, input().split())

ans = 0
for i in range(1, n+1):
  tmp = 1 / n
  if i < k:
    tmp *= 0.5 ** ceil(log2(k/i))
  ans += tmp

print(ans)
