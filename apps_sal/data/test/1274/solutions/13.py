import heapq
n, m = map(int, input().split())
d = [[] for _ in range(m)]
for _ in range(n):
    a, b = map(int, input().split())
    if a <= m:
        d[a-1].append(-b)

t = []
heapq.heapify(t)
ans = 0
for i in range(m):
    for dd in d[i]:
        heapq.heappush(t, dd)
    if t:
        ans += heapq.heappop(t)*(-1)
print(ans)
