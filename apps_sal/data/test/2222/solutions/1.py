from collections import defaultdict
from collections import deque
n = int(input())
tree = defaultdict(set)
node_type = list(map(int, input().split()))
values = [0 for x in range(n)]
for i, x in enumerate(map(int, input().split())):
    tree[x - 1].add(i + 1)

queue = deque([(0, False)])
while queue:
    node, tag = queue.popleft()
    if not node in tree:
        values[node] = 1
        continue
    elif tag:
        if node_type[node]:
            values[node] = min(values[c] for c in tree[node])
        else:
            values[node] = sum(values[c] for c in tree[node])
    else:
        queue.appendleft((node, True))
        queue.extendleft((c, False) for c in tree[node])
k = n - len(tree)
print(k - values[0] + 1)
