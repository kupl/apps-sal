from collections import defaultdict
import heapq
def inpl(): return list(map(int, input().split()))


N, M = inpl()
Edge = defaultdict(lambda: [])
for _ in range(M):
    a, b = inpl()
    if a != b:
        Edge[a].append(b)
        Edge[b].append(a)
Ans = []
visited = set([1])
Candi = [1]
for _ in range(N):
    j = heapq.heappop(Candi)
    for k in Edge[j]:
        if k not in visited:
            visited.add(k)
            heapq.heappush(Candi, k)
    Ans.append(j)
print(*Ans)
