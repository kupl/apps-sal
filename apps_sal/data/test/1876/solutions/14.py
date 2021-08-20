from collections import deque
mod = 10 ** 9 + 7


class TreeNode:

    def __init__(self, val):
        self.val = val
        self.edges = {}

    def add_edge(self, node, color):
        self.edges[node] = color


(n, k) = list(map(int, input().split()))
tree = []
for i in range(1, n + 1):
    tree.append(TreeNode(i))
for _ in range(n - 1):
    (u, v, x) = list(map(int, input().split()))
    tree[u - 1].add_edge(v, x)
    tree[v - 1].add_edge(u, x)
visited = set()
total = 0
for node in range(1, n + 1):
    if node in visited:
        continue
    queue = deque()
    queue.append(node)
    visited.add(node)
    red_vertexes = 1
    while queue:
        vertex = queue.popleft()
        for (e, c) in list(tree[vertex - 1].edges.items()):
            if c == 0 and e not in visited:
                queue.append(e)
                red_vertexes = red_vertexes + 1
                visited.add(e)
    total = (total + pow(red_vertexes, k, mod)) % mod
total = (pow(n, k, mod) - total) % mod
print(total)
