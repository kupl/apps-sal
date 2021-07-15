# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N,M = map(int,input().split())
ABC = [list(map(int,input().split())) for _ in range(M)]

g = [[0 for _ in range(N)] for _ in range(N)]

for a,b,c in ABC:
    g[a-1][b-1] = c

from scipy.sparse.csgraph import csgraph_from_dense, floyd_warshall
csg = csgraph_from_dense(g)
d = floyd_warshall(csg, directed=False)

ans = 0
for a,b,c in ABC:
    if c != d[a-1][b-1]:
        ans += 1

print(ans)
