# import time

def set_color(edge, colors, color):
    colors[edge] = color
    colors[(edge[1], edge[0])] = color

def set_node_color(node, parent, parent_color, index, bad_nodes, colors):
    color = 1
    for child_node in (child for child in index[node] if child != parent):
        if color == parent_color:
            color += 1
        new_color = parent_color if node in bad_nodes else color
        color += 1
        set_color((node, child_node), colors, new_color)
        set_node_color(child_node, node, new_color, index, bad_nodes, colors)

def solve(n, k, edges):
    colors = {edge: None for edge in edges}
    index = {i : set() for i in range(1, n + 1)}
    for a, b in edges:
        index[a].add(b)
        index[b].add(a)
    nodes = sorted(list(range(1, n + 1)), key=lambda x: len(index[x]), reverse=True)
    bad_nodes = set(nodes[:k])

    frontier = [(nodes[k], None, None)]
    while frontier:
        # print(len(frontier))
        next_, parent_node, parent_color = frontier.pop()
        # print('pop:', next_)
        color = 1
        for child_node in (ele for ele in index[next_] if ele != parent_node):
            if color == parent_color:
                color += 1
            new_color = parent_color if next_ in bad_nodes else color
            set_color((next_, child_node), colors, new_color)
            color += 1
            frontier.append((child_node, next_, new_color))
            # print('append:', child_node)

    # set_node_color(nodes[k], None, None, index, bad_nodes, colors)
    return [colors[edge] for edge in edges]

def main():
    n, k = map(int, input().split())
    edges = []
    for i in range(n - 1):
        edges.append(tuple(map(int, input().split())))
    # n, k = 200000, 0
    # edges = [(n, n + 1) for n in range(1, n)]
    # n, k = 6, 2
    # edges = [(1, 4), (4, 3), (3, 5), (3, 6), (5, 2)]
    # tick = time.time()
    result = solve(n, k, edges)
    print(len(set(result)))
    print(' '.join(map(str, result)))
    # tock = time.time()
    # print('T:', round(tock - tick, 5))

def __starting_point():
    main()
__starting_point()
