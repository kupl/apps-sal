def is_valid():
    import sys
    with sys.stdin as f:
        for i, line in enumerate(f):
            if i == 0:
                N, M = line.split(' ')
                N, M = int(N), int(M)
                if N - 1 != M:
                    return False
                graph = [[] for _ in range(N)]
            else:
                fromVertex, toVertex = line.split(' ')
                fromVertex, toVertex = int(fromVertex) - 1, int(toVertex) - 1
                graph[fromVertex].append(toVertex)
                graph[toVertex].append(fromVertex)

    from queue import LifoQueue

    def is_single_component(start_node, graph):
        N = len(graph)
        visited = [False for _ in range(N)]
        visited[start_node] = True
        nodes_queue = LifoQueue()
        nodes_queue.put(start_node)
        while not nodes_queue.empty():
            node = nodes_queue.get()
            for neigh in graph[node]:
                if not visited[neigh]:
                    visited[neigh] = True
                    nodes_queue.put(neigh)

        return all(visited)

    return is_single_component(0, graph)


if is_valid():
    print("yes")
else:
    print("no")
