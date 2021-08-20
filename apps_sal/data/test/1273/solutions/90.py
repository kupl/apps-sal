from collections import deque
N = int(input())
tree = [[] for i in range(N)]
key_order = [0] * (N - 1)
for i in range(N - 1):
    (in1, in2) = map(int, input().split())
    in1 -= 1
    in2 -= 1
    tree[in1].append(in2)
    tree[in2].append(in1)
    key_order[i] = (in1, in2)


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
                edge_colors[q, v] = cnt
                node_colors[v] = cnt
                queue.append(v)
                cnt += 1
    '\n    node_colors = [set() for _ in tree]\n    edge_colors = dict()\n    all_colors = set()\n    color = 0\n\n    while len(queue) > 0:\n        q = queue.popleft()\n        seen[q] = True\n\n        for v in tree[q]:\n            if not seen[v]:\n                residual = all_colors - node_colors[q]\n                if len(residual) > 0:\n                    this_color = residual.pop()\n                else:\n                    color += 1\n                    this_color = color\n                edge_colors[(q, v)] = this_color\n                node_colors[q].add(this_color)\n                node_colors[v].add(this_color)\n                all_colors.add(this_color)\n\n                queue.append(v)\n    '
    return edge_colors


edge_colors = bfs(tree, 0)
print(max([c for (key, c) in edge_colors.items()]))
[print(edge_colors[t]) for t in key_order]
