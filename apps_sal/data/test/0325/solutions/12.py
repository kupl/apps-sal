from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import bellman_ford, NegativeCycleError
import sys
input = sys.stdin.readline


def main():
    n, m, p = list(map(int, input().split()))

    edges = []
    routes = [[] for _ in range(n)]
    rev_routes = [[] for _ in range(n)]

    def get_reachable_nodes(start, routes):
        seen = {start}
        todo = []
        for to in routes[start]:
            todo.append(to)
            seen.add(to)

        while todo:
            node = todo.pop()
            for to in routes[node]:
                if to in seen:
                    continue
                todo.append(to)
                seen.add(to)
        return seen

    for _ in range(m):
        node1, node2, value = list(map(int, input().split()))
        node1, node2, value = node1 - 1, node2 - 1, value - p
        edges.append([node1, node2, value])
        routes[node1].append(node2)
        rev_routes[node2].append(node1)

    from_start = get_reachable_nodes(0, routes)
    if n-1 not in from_start:
        print((-1))
        return

    to_goal = get_reachable_nodes(n-1, rev_routes)

    from_start_to_goal = from_start & to_goal

    temp_dict = dict()

    for row, col, value in edges:
        if {row, col} <= from_start_to_goal:
            if not (row, col) in temp_dict:
                temp_dict[(row, col)] = -value
            else:
                temp_dict[(row, col)] = min(-value, temp_dict[(row, col)])

    values = []
    rows = []
    cols = []

    for (row, col), minus_value in list(temp_dict.items()):
        values.append(minus_value)
        rows.append(row)
        cols.append(col)

    graph = coo_matrix((values, (rows, cols)), shape=(n, n))
    try:
        bf = bellman_ford(graph, indices=[0])
        print((max(0, -int(bf[0][n - 1]))))
    except NegativeCycleError:
        print((-1))


def __starting_point():
    main()

__starting_point()
