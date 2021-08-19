from collections import defaultdict, deque, Counter
N = int(input())
counter = Counter()
nodes = defaultdict(list)
edges = []
for i in range(N - 1):
    (u, v) = list(map(int, input().split(' ')))
    nodes[u].append((v, i))
    nodes[v].append((u, i))
    edges.append((u, v))
K = 0
for node in list(nodes.values()):
    K = max(K, len(node))
checked = set()
queue = deque([(1, 0)])
edge_colors = [0] * N
while queue:
    (u, uc) = queue.popleft()
    checked.add(u)
    color = 1
    for (v, e) in nodes[u]:
        if v in checked:
            continue
        if color == uc:
            color += 1
        edge_colors[e] = color
        queue.append((v, color))
        color += 1
print(K)
for i in range(N - 1):
    print(edge_colors[i])
