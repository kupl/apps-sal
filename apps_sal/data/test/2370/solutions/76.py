import numpy as np
from scipy.sparse.csgraph import floyd_warshall
INF = 10**9

n = int(input())
a = np.array([list(map(int, input().split())) for _ in range(n)])
a_opt = floyd_warshall(a)
# for i in range(n): print(a[i], a_opt[i])

for i in range(n):
    a[i][i] = INF
    
ans = 0
for i in range(n):
    for j in range(i+1, n):
        if a_opt[i][j] < a[i][j]:
            print((-1))
            return
        else:
            d = a[i][j]
            if d < np.min(a[i]+a[j]):
                ans += d
                
            # Straight solution, but TLE in python
            # for k in range(n):
            #     if k in [i, j]:
            #         continue
            #     elif a[i][k]+a[k][j] == d:
            #         d = 0
            # ans += d
print(ans)

