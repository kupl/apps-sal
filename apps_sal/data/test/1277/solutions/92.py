import numpy as np
import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
N, u, v = map(int, input().split())

E = [[] for _ in range(N+1)]
for _ in range(N-1):
	ta, tb = map(int, input().split())
	E[ta].append(tb)
	E[tb].append(ta)
E = np.array(E)

inf = 10**9
taka = np.full(N+1, inf, dtype = np.int64)
ao = np.full(N+1, inf, dtype = np.int64)
taka[u] = 0
ao[v] = 0
def solve(dist, start):
	q = [start]
	while q:
		cp = q.pop()
		for nep in E[cp]:
			if dist[nep] != inf:
				continue
			else:
				dist[nep] = dist[cp] + 1
				q.append(nep)

solve(taka, u)
solve(ao, v)
ind = taka < ao
ao_max = np.max(ao[ind])
print(ao_max - 1)
