import sys
K = int(input())

graph = [[] for _ in range(K)]
for i in range(K):
    graph[i].append(((i + 1) % K, 1))
    graph[i].append(((10 * i) % K, 0))

dist = [-1] * K
s, t = 1, 0
queue = [s]
d = 0
while queue:
    new_queue = set()

    while queue:
        q = queue.pop()
        if dist[q] == -1:
            dist[q] = d
            for v, w in graph[q]:
                if w == 0:
                    queue.append(v)
                else:
                    new_queue.add(v)

    d += 1
    queue = list(new_queue)

print(dist[0] + 1)
