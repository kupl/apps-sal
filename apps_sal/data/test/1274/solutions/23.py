import heapq
n, m = map(int, input().split())
ab = [0] * n
V = [[] for i in range(m + 1)]
for i in range(n):
    a, b = map(int, input().split())
    if a <= m:
        V[a].append(-b)

q = []
ans = 0
heapq.heapify(q)
for i in range(1, m + 1):
    for v in V[i]:
        heapq.heappush(q, v)

    if len(q) == 0:
        pass
    else:
        ans -= heapq.heappop(q)
print(ans)
