from collections import deque
from typing import List


def get_longest_path_depth(
    graph: List[List[int]], in_degrees: List[int], first_index: int = 0
) -> int:
    """Return the depth of the longest path of DAG.
    if the given graph is not DAG, -1 is returned.
    """
    V = len(graph) + first_index
    queue = deque()
    depths = [-1] * V
    for i in range(first_index, V):
        if not in_degrees[i]:
            queue.append(i)
            depths[i] = 0

    while queue:
        u = queue.popleft()
        cur_depth = depths[u]
        for v in graph[u]:
            in_degrees[v] -= 1
            if not in_degrees[v]:
                depths[v] = max(depths[v], cur_depth + 1)
                queue.append(v)

    return max(depths[first_index:]) if min(depths[1:]) != -1 else -1


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

    depth = get_longest_path_depth(graph, in_degrees)
    print((depth + 1 if depth != -1 else -1))


def __starting_point():
    abc139_e()


__starting_point()
