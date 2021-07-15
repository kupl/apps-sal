from collections import defaultdict
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree


class Point:
 
    def __init__(self, index, x, y):
        self.index = index
        self.x = x
        self.y = y


def create_graph(N, points):
    # Caclulate costs
    costs = defaultdict(int)
    costs_defined = defaultdict(int)
    # Sort by `x` and create edges between adjacent nodes
    points = sorted(points, key=lambda p: p.x)
    for i in range(N - 1):
        p = points[i]
        next_p = points[i + 1]
        cost = next_p.x - p.x
        min_index, max_index = min([p.index, next_p.index]), max([p.index, next_p.index])
        costs[(min_index, max_index)] = cost
        costs_defined[(min_index, max_index)] = 1
    # Sort by `y` and create edges between adjacent nodes
    points = sorted(points, key=lambda p: p.y)
    for i in range(N - 1):
        p = points[i]
        next_p = points[i + 1]
        cost = next_p.y - p.y
        min_index, max_index = min([p.index, next_p.index]), max([p.index, next_p.index])
        current_cost = costs[(min_index, max_index)]
        if costs_defined[(min_index, max_index)]:
            new_cost = min([cost, current_cost])
            costs[(min_index, max_index)] = new_cost
        else:
            costs[(min_index, max_index)] = cost
    # Create csgraph
    rows = list()
    cols = list()
    data = list()
    for node_pair, cost in costs.items():
        rows.append(node_pair[0])
        cols.append(node_pair[1])
        data.append(cost)
    return csr_matrix((data, (rows, cols)), shape=(N, N))

 
def main():
    N = int(input())
    points = list()
    for index in range(N):
        x, y = list(map(int, input().split(' ')))
        points.append(Point(index, x, y))
    graph = create_graph(N, points)
    mst = minimum_spanning_tree(graph)
    print(int(mst.sum()))
 
 
def __starting_point():
    main()
__starting_point()
