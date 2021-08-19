import heapq
(n, m) = list(map(int, input().split()))
d = [[] for _ in range(m + 1)]
for _ in range(n):
    (a, b) = list(map(int, input().split()))
    if a < m + 1:
        d[a].append(b)
hq = []
heapq.heapify(hq)
ans = 0
for i in range(1, m + 1):
    if len(d[i]) > 0:
        for j in d[i]:
            heapq.heappush(hq, j * -1)
    if len(hq) > 0:
        ans += heapq.heappop(hq) * -1
print(ans)
