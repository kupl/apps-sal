class Vertex:
    def __init__(self, index):
        self.index = index
        self.neighbours = []
        self.color = None


def main():

    n = int(input())
    cols = []
    cols.append([int(z) for z in input().split()])
    cols.append([int(z) for z in input().split()])
    cols.append([int(z) for z in input().split()])

    tree = [Vertex(i) for i in range(n)]

    for _ in range(n-1):
        u1, u2 = [int(p) - 1 for p in input().split()]
        tree[u1].neighbours.append(u2)
        tree[u2].neighbours.append(u1)

    if any(len(vertex.neighbours) > 2 for vertex in tree):
        print("-1")
        return

    root = None
    for vertex in tree:
        if len(vertex.neighbours) == 1:
            root = vertex
            break

    current_group = 1
    prev_vertex = root.index
    vertex = tree[root.neighbours[0]]
    groups = [[root.index], [], []]

    while True:
        is_leaf = len(vertex.neighbours) == 1
        groups[current_group].append(vertex.index)
        if is_leaf:
            break
        current_group = (current_group + 1) % 3
        next_vertex_index = sum(vertex.neighbours) - prev_vertex
        prev_vertex = vertex.index
        vertex = tree[next_vertex_index]

    best_col_per_group = None
    best_price = None
    for col_per_group in [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]:
        price = 0
        for group_id in range(len(groups)):
            group_col = col_per_group[group_id] - 1
            for node_id in groups[group_id]:
                price += cols[group_col][node_id]
        if best_price is None or price < best_price:
            best_price = price
            best_col_per_group = col_per_group

    print(best_price)
    for color, group in zip(best_col_per_group, groups):
        for node_id in group:
            tree[node_id].color = color

    for node in tree:
        print(node.color, end=' ')

main()
