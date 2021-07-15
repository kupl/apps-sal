import collections
n = int(input())
a = list(map(int, input().split()))

to = {}
for i, node in enumerate(a):
    to[i+2] = node

layers = collections.defaultdict(list)
for k, v in to.items():
    layers[v].append(k)

queue = [1]
ans = 0
while queue:
    ans += len(queue)%2
    n = len(queue)
    for _ in range(n):
        node = queue.pop(0)
        if node in layers:
            queue.extend(layers[node])

print(ans)
