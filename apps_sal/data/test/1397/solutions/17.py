(n, m) = [int(x) for x in input().split(' ')]
free_nodes = [True] * n
for _ in range(m):
    (source, dest) = [int(x) for x in input().split(' ')]
    (free_nodes[source - 1], free_nodes[dest - 1]) = (False, False)
first_free_node = free_nodes.index(True) + 1
print(n - 1)
other_nodes = [x for x in range(1, n + 1) if x != first_free_node]
for node in other_nodes:
    print('{0} {1}'.format(first_free_node, node))
