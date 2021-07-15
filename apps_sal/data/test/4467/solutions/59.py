import networkx as nx

n = int(input())
graph = nx.DiGraph()
AB = [list(map(int, input().split())) for _ in range(n)]
CD = [list(map(int, input().split())) for _ in range(n)]

start = 10 ** 4
goal = 10 ** 4 + 1
for i in range(n):
    a, b = AB[i]
    graph.add_edge(start, i, weight=0, capacity=1)
    for j in range(n):
        c, d = CD[j]
        graph.add_edge(200 + j, goal, weight=0, capacity=1)
        if c > a and d > b:
            graph.add_edge(i, 200 + j, weight=0, capacity=1)

ans = nx.maximum_flow(graph, start, goal, capacity="capacity")
print((ans[0]))


