import sys
INF = 1 << 60
MOD = 10**9 + 7 # 998244353
sys.setrecursionlimit(2147483647)
input = lambda:sys.stdin.readline().rstrip()
import networkx as nx
def resolve():
    n = int(input())
    A = [tuple(map(int, input().split())) for _ in range(n)]
    B = [tuple(map(int, input().split())) for _ in range(n)]
    G = nx.Graph()
    G.add_nodes_from(range(n))
    G.add_nodes_from(range(n, 2 * n))
    for i in range(n):
        ax, ay = A[i]
        for j in range(n):
            bx, by = B[j]
            if ax < bx and ay < by:
                G.add_edge(i, n + j)

    A = nx.algorithms.bipartite.matching.hopcroft_karp_matching(G, top_nodes = range(n))
    print(len(A) // 2)
resolve()
