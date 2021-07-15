import numpy as np

n = int(input())
a = np.array([int(x) for x in input().split()])

ans = 0
mod = pow(10, 9)+7
for i in range(100):
  c = np.sum((a>>i)&1)
  ans += (c*(n-c)%mod)*pow(2, i, mod)%mod
  ans %= mod

print(ans)
