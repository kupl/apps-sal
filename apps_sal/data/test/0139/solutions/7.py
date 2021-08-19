import sys
input = sys.stdin.readline


def get_input():
    (n, m) = [int(x) for x in input().split(' ')]
    digraph = [[] for _ in range(n + 1)]
    for _ in range(m):
        (c1, c2) = [int(x) for x in input().split(' ')]
        digraph[c1].append(c2)
    return digraph


def dfs(graph, u=-1, v=-1):
    n = len(graph)
    pi = [None] * n
    color = ['white'] * n
    for node in range(1, n):
        if color[node] == 'white':
            cicle = dfs_visit(graph, node, color, pi, u, v)
            if cicle is not None:
                return cicle
    return None


def dfs_visit(graph, root, color, pi, u, v):
    stack = [root]
    while stack:
        current_node = stack[-1]
        if color[current_node] != 'white':
            stack.pop()
            color[current_node] = 'black'
            continue
        color[current_node] = 'grey'
        for adj in graph[current_node]:
            if (current_node, adj) == (u, v):
                continue
            if color[adj] == 'white':
                pi[adj] = current_node
                stack.append(adj)
            elif color[adj] == 'grey':
                cicle = [adj]
                while current_node != adj:
                    cicle.append(current_node)
                    current_node = pi[current_node]
                cicle.append(adj)
                return cicle
    return None


def __starting_point():
    digraph = get_input()
    cicle = dfs(digraph)
    if cicle is None:
        print('YES')
    else:
        cicle.reverse()
        for i in range(len(cicle) - 1):
            c = dfs(digraph, cicle[i], cicle[i + 1])
            if c is None:
                print('YES')
                break
        else:
            print('NO')


__starting_point()
