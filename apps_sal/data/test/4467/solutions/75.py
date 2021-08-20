from scipy.sparse.csgraph import maximum_bipartite_matching
from scipy.sparse import coo_matrix
import sys
INF = 1 << 60
MOD = 10 ** 9 + 7
sys.setrecursionlimit(2147483647)


def input():
    return sys.stdin.readline().rstrip()


def resolve():
    n = int(input())
    A = [tuple(map(int, input().split())) for _ in range(n)]
    B = [tuple(map(int, input().split())) for _ in range(n)]
    weights = []
    rows = []
    columns = []
    for i in range(n):
        (ax, ay) = A[i]
        for j in range(n):
            (bx, by) = B[j]
            if ax < bx and ay < by:
                weights.append(1)
                rows.append(i)
                columns.append(j)
    graph = coo_matrix((weights, (rows, columns)), shape=(n, n))
    ans = sum(maximum_bipartite_matching(graph) >= 0)
    print(ans)


resolve()
