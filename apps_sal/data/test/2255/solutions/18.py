import sys
import collections
import heapq
data = sys.stdin.read().splitlines()
(n, m) = list(map(int, data[0].split()))
graph = collections.defaultdict(set)
for line in data[1:]:
    (a, b) = list(map(int, line.split()))
    graph[a].add(b)
    graph[b].add(a)
for node in graph:
    graph[node] = sorted(graph[node], reverse=True)
visited = [False] * (n + 1)
visited[1] = True
ans = []
queue = [1]
while True:
    cur = heapq.heappop(queue)
    ans.append(cur)
    if len(ans) == n:
        break
    for nei in graph[cur]:
        if not visited[nei]:
            visited[nei] = True
            heapq.heappush(queue, nei)
print(' '.join(map(str, ans)))
