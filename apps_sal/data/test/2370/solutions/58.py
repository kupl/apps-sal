import numpy as np

n = int(input())
a = np.array([np.array(input().split(), dtype=np.uint64) for _ in range(n)], dtype=np.uint64)

for i in range(n):
  a[i,i] = 1e9 + 1

ans = 0
for u in range(n):
    for v in range(u + 1, n): 
        dist = a[u,v]
        cd = np.min(a[u] + a[v])
        if dist > cd:
            print(-1)
            return
        if dist < cd:
            ans += dist
 
print(int(ans))
