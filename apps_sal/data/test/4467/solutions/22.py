import sys
INF = 1 << 60
MOD = 10**9 + 7 # 998244353
sys.setrecursionlimit(2147483647)
input = lambda:sys.stdin.readline().rstrip()
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import maximum_bipartite_matching
def resolve():
    n = int(input())
    A = [tuple(map(int, input().split())) for _ in range(n)]
    B = [tuple(map(int, input().split())) for _ in range(n)]

    graph = csr_matrix([[int(A[i][0] < B[j][0] and A[i][1] < B[j][1]) for j in range(n)] for i in range(n)])
    ans = 0
    for a in maximum_bipartite_matching(graph):
        if a != -1:
            ans += 1
    print(ans)
resolve()
