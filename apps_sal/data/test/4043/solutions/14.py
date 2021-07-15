
def construct_tree(n,d, k):
    nodes = []
    edges = []

    if d > n - 1:
        return None
    
    if k == 1 and n > 2:
        return None

    for i in range(1, d+2):
        current_deg = k - 1 if i == 1 or i == d + 1 else k - 2
        current_depth =  min(i-1, d-i+1)
        if current_depth and current_deg:
            nodes.append([i, min(i-1, d-i+1), current_deg])
        if i < d + 1:
            edges.append([i, i+1])

    current_nodes_count = d + 2
    pos = 0
    while current_nodes_count < n + 1:

        if pos >= len(nodes):
            return None

        current = nodes[pos]

        if not current[2]:
            pos += 1
            if pos == len(nodes):
                break
            continue

        if current[1] - 1 and k - 1:
            nodes.append([current_nodes_count, current[1] - 1, k - 1])
        edges.append([current[0], current_nodes_count])
        current[2] -= 1
        current_nodes_count += 1
    
    if current_nodes_count == n + 1:
        return edges
    return None



n, d, k = [int(val) for val in input().split()]
edges = construct_tree(n, d, k)
if edges:
    print('YES')
    print('\n'.join(['{0} {1}'.format(e[0], e[1]) for e in edges]))
else:
    print('NO')


