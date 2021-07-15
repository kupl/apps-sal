from collections import deque

N = int(input())
# mtx = np.zeros([N, N], dtype=np.int32)
tree = [[] for i in range(N)]

key_order = [0] * (N-1)
for i in range(N-1):
    in1, in2 = map(int, input().split())
    in1 -= 1
    in2 -= 1
    tree[in1].append(in2)
    tree[in2].append(in1)

    key_order[i] = (in1, in2)

# [print(i, t) for i, t in enumerate(tree)]


def bfs(tree, p):
    seen = [False] * len(tree)
    queue = deque((p,))

    edge_colors = dict()
    node_colors = [0] * len(tree)
    while len(queue) > 0:
        q = queue.popleft()
        seen[q] = True

        parent_color = node_colors[q]

        cnt = 1
        for v in tree[q]:
            if not seen[v]:
                if cnt == parent_color:
                    cnt += 1

                edge_colors[(q, v)] = cnt
                node_colors[v] = cnt
                queue.append(v)
                cnt += 1



    """
    node_colors = [set() for _ in tree]
    edge_colors = dict()
    all_colors = set()
    color = 0

    while len(queue) > 0:
        q = queue.popleft()
        seen[q] = True

        for v in tree[q]:
            if not seen[v]:
                residual = all_colors - node_colors[q]
                if len(residual) > 0:
                    this_color = residual.pop()
                else:
                    color += 1
                    this_color = color
                edge_colors[(q, v)] = this_color
                node_colors[q].add(this_color)
                node_colors[v].add(this_color)
                all_colors.add(this_color)

                queue.append(v)
    """

    return edge_colors


edge_colors = bfs(tree, 0)

print(max([c for key, c in edge_colors.items()]))
[print(edge_colors[t]) for t in key_order]
# print(edge_colors)

# show_tree(tree)

