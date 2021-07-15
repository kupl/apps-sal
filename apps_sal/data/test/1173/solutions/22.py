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
    depths = [0] * V  # depths[i] := the length of the longest path to V_i
    order = [i for i in range(first_index, V) if not in_degrees[i]]
    queue = deque(order)

    while queue:
        u = queue.popleft()
        cur_depth = depths[u]
        for v in graph[u]:
            in_degrees[v] -= 1
            if not in_degrees[v]:
                depths[v] = cur_depth + 1
                queue.append(v), order.append(v)

    return (order, depths) if len(order) + first_index == V else (None, None)


def abc139_e():
    # https://atcoder.jp/contests/abc139/tasks/abc139_e
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
    print((max(depths) + 1 if depths else -1))


def grl_4_a():
    # https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/4/GRL_4_A
    V, _, *ST = list(map(int, open(0).read().split()))
    graph = [[] for _ in range(V)]
    in_degrees = [0] * V
    for s, t in zip(*[iter(ST)] * 2):
        graph[s].append(t)
        in_degrees[t] += 1

    res, _ = cycle_detectable_topological_sort(graph, in_degrees)
    print((1 if res is None else 0))


def __starting_point():
    abc139_e()
    # grl_4_a()

__starting_point()
