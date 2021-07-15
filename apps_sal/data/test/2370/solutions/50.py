import numpy as np
from scipy.sparse.csgraph import floyd_warshall
n = int(input())
a = np.array([[int(i) for i in input().split()] for i in range(n)])
d,ans = floyd_warshall(a,directed=False),0
if any(a[i][j]!=d[i][j] for i in range(n) for j in range(n)): ans = -1
else:
	inf = 10**10
	for i in range(n): a[i][i] = inf
	for i in range(n):
		for j in range(i+1,n):
			num = np.min(a[i]+a[j])
			if num>a[i][j]: ans+=a[i][j]
print(int(ans))
