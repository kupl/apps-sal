from collections import deque
from typing import List, Optional, Tuple


def cycle_detectable_topological_sort(
    graph: List[List[int]], in_degrees: List[int], first_index: int = 0
) -> Tuple[Optional[List[int]], Optional[List[int]]]:
    """Topological sort that uses Kahn's algorithm and detects a loop (DAG or not).
    Returns:
        if the given graph is DAG, a list of sorted vertices and a list of depths of
        each vertex is returned.
        Otherwise, (None, None) is returned.
    """
    V = len(graph) + first_index
    order = []
    depths = [-1] * V  # depths[i] := the length of the longest path to V_i
    for i in range(first_index, V):
        if not in_degrees[i]:
            order.append(i)
            depths[i] = 0

    queue = deque(order)
    while queue:
        u = queue.popleft()
        cur_depth = depths[u]
        for v in graph[u]:
            in_degrees[v] -= 1
            if not in_degrees[v]:
                depths[v] = max(depths[v], cur_depth + 1)
                queue.append(v), order.append(v)
    return (order, depths) if len(order) + first_index == V else (None, None)


def abc139_e():
    N, *A = list(map(int, open(0).read().split()))

    ids = [[-1] * (N + 1) for _ in range(N + 1)]
    cur_id = 0
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            ids[i][j] = ids[j][i] = cur_id
            cur_id += 1

    graph = [[] for _ in range(N * (N - 1) // 2)]
    in_degrees = [0] * (N * (N - 1) // 2)
    for i, a in enumerate(zip(*[iter(A)] * (N - 1)), 1):
        source = -1
        for j in a:
            target = ids[i][j]
            if source != -1:
                graph[source].append(target)
                in_degrees[target] += 1
            source = target

    _, depths = cycle_detectable_topological_sort(graph, in_degrees)
    print((max(depths) + 1 if depths is not None else -1))


def __starting_point():
    abc139_e()

__starting_point()
