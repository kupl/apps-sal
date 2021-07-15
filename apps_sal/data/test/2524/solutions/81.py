import numpy as np
n,*a = map(int,open(0).read().split())
a = np.array(a)
mod = 10**9+7
ans = 0
for i in range(61):
  b = np.count_nonzero(a>>i&1)
  ans += b*(n-b)*1<<i
print(ans%mod)
