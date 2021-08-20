import sys
with sys.stdin as f:
    for (i, line) in enumerate(f):
        if i == 0:
            (N, M) = line.split(' ')
            (N, M) = (int(N), int(M))
            graph = [[] for _ in range(N)]
        else:
            (fromVertex, toVertex) = line.split(' ')
            (fromVertex, toVertex) = (int(fromVertex) - 1, int(toVertex) - 1)
            graph[fromVertex].append(toVertex)
            graph[toVertex].append(fromVertex)
from queue import Queue


def farthest_node_distance(start_node, graph):
    """ returns farthest node from start node and its distance """
    N = len(graph)
    visited = [False for _ in range(N)]
    distances = [-1 for _ in range(N)]
    visited[start_node] = True
    distances[start_node] = 0
    nodes_queue = Queue()
    nodes_queue.put(start_node)
    while not nodes_queue.empty():
        node = nodes_queue.get()
        for neigh in graph[node]:
            if not visited[neigh]:
                visited[neigh] = True
                distances[neigh] = distances[node] + 1
                nodes_queue.put(neigh)
    return (node, distances[node])


(u, dist_u) = farthest_node_distance(0, graph)
(v, dist_uv) = farthest_node_distance(u, graph)
print(dist_uv)
