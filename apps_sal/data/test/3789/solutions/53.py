import sys
INF = 1 << 60
MOD = 10**9 + 7 # 998244353
sys.setrecursionlimit(2147483647)
input = lambda:sys.stdin.readline().rstrip()
import networkx as nx
def resolve():
    n = int(input())
    A = list(map(int, input().split()))
    total = sum(a for a in A if a > 0)

    # minimum cut
    G = nx.DiGraph()
    G.add_nodes_from(range(1, n + 1))
    G.add_nodes_from(["source", "termination"])
    for i, a in enumerate(A, 1):
        if a >= 0:
            G.add_edge("source", i, capacity = 0)
            G.add_edge(i, "termination", capacity = a)
        else:
            G.add_edge("source", i, capacity = -a)
            G.add_edge(i, "termination", capacity = 0)

    for i in range(1, n + 1):
        for j in range(2 * i, n + 1, i):
            G.add_edge(i, j, capacity = INF)

    flow = nx.algorithms.flow.maximum_flow_value(G, "source", "termination")
    print(total - flow)
resolve()
