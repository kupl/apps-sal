import numpy as np
n=int(input())
l=[np.array(input().split(), dtype=np.int64) for _ in [0]*n]
l+=np.diag([10**10]*n)

v=0
for i in range(n-1):
  for j,d1 in enumerate(l[i][i+1:]):
    d2=np.min(l[i]+l[j+i+1])
    if d1>=d2:
      if d1>d2:
        print(-1)
        return
    else:
      v+=d1
print(v)
