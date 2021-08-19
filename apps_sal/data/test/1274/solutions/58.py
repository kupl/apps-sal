import heapq
(n, m) = map(int, input().split())
limit = [[] for i in range(m)]
for i in range(n):
    (a, b) = map(int, input().split())
    if a > m:
        continue
    limit[m - a].append(b)
available = []
ans = 0
for i in range(m - 1, -1, -1):
    for item in limit[i]:
        heapq.heappush(available, -item)
    if available:
        ans += -heapq.heappop(available)
print(ans)
