import sys
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import floyd_warshall
from itertools import permutations
input = sys.stdin.readline
ans = -1
(n, m, r) = list(map(int, input().split()))
r = list(map(int, input().split()))
(A, B, C) = ([], [], [])
for i in range(m):
    (a, b, c) = list(map(int, input().split()))
    A.append(a - 1)
    B.append(b - 1)
    C.append(c)
wf = floyd_warshall(csr_matrix((C, (A, B)), shape=(n, n)), directed=False)
for pi in permutations(r):
    cand = 0
    for (r1, r2) in zip(pi, pi[1:]):
        cand += int(wf[r1 - 1][r2 - 1])
    if ans < 0 or ans > cand:
        ans = cand
print(ans)
