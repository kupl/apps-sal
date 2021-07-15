import numpy as np
n,m = map(int, input().split())
ans = np.zeros(n, dtype=int)
for i in range(m):
    a,b = map(int, input().split())
    ans[a-1] += 1
    ans[b-1] += 1
for i in range(n):
    print(ans[i])
