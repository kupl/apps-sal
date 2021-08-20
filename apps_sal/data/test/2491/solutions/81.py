from collections import defaultdict
(n, m) = map(int, input().split())
G = defaultdict(dict)
for i in range(1, n):
    G[i + 1] = {}
for i in range(m):
    (a, b, c) = map(int, input().split())
    G[a][b] = c
start_vertex = 1


def bellmanford(G, start_vertex):
    if start_vertex not in G:
        return (-1, -1)
    distances = {}
    parents = {}
    for node in G:
        distances[node] = float('-inf')
        parents[node] = None
    distances[start_vertex] = 0
    for _ in range(len(G) - 1):
        for node in G.keys():
            for neighbor in G[node]:
                if distances[neighbor] < distances[node] + G[node][neighbor]:
                    distances[neighbor] = distances[node] + G[node][neighbor]
                    parents[neighbor] = node
    pathnode = n
    while pathnode != start_vertex:
        for neighbor in G[pathnode]:
            if distances[neighbor] < distances[pathnode] + G[pathnode][neighbor]:
                print('inf', flush=True)
                return (-1, -1)
        pathnode = parents[pathnode]
    return (distances, parents)


(distances, parents) = bellmanford(G, start_vertex)
if distances != -1:
    print(distances[n], flush=True)
