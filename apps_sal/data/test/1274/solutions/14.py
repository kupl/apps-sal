import heapq
(n, m) = map(int, input().split())
x = [[] for _ in range(m + 1)]
y = []
heapq.heapify(y)
for i in range(1, m + 1):
    heapq.heapify(x[i])
for _ in range(n):
    (a, b) = map(int, input().split())
    if a <= m:
        heapq.heappush(x[a], -b)
ans = 0
for i in range(1, m + 1):
    if x[i]:
        s = heapq.heappop(x[i])
        heapq.heappush(y, [s, i])
    if y:
        (s, t) = heapq.heappop(y)
        ans -= s
        if x[t]:
            s = heapq.heappop(x[t])
            heapq.heappush(y, [s, t])
print(ans)
