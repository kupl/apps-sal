import networkx as nx
import sys
INF = 1 << 60
MOD = 10**9 + 7
sys.setrecursionlimit(2147483647)
def input(): return sys.stdin.readline().rstrip()


def resolve():
    m, n = map(int, input().split())
    G = nx.Graph()
    G.add_nodes_from(range(m + n + 2))
    for i in range(m):
        for j, c in enumerate(input()):
            if c == '.':
                continue
            elif c == 'o':
                G.add_edge(i, m + j, capacity=1)
            elif c == 'S':
                G.add_edge(-1, i, capacity=INF)
                G.add_edge(-1, m + j, capacity=INF)
            elif c == 'T':
                G.add_edge(i, m + n, capacity=INF)
                G.add_edge(m + j, m + n, capacity=INF)

    ans = nx.algorithms.flow.maximum_flow_value(G, -1, m + n)
    if ans >= INF:
        ans = -1
    print(ans)


resolve()
