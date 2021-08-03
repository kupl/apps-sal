import heapq

n, m = map(int, input().split())
ab = [[] * (m + 1) for i in range(m + 1)]
for i in range(n):
    a, b = map(int, input().split())
    if m - a < 0:
        continue
    ab[a].append(b)

q = []
ans = 0
heapq.heapify(q)
for i in range(1, m + 1):
    for j in ab[i]:
        heapq.heappush(q, j * (-1))
    if q:
        b = heapq.heappop(q)
        ans += (-1) * b
print(ans)
