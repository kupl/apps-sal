import heapq
n, m = map(int, input().split())
kouho = [[] for i in range(m)]
for i in range(n):
    a, b = map(int, input().split())
    if a <= m:
        kouho[a - 1].append(-b)
ans = 0
p = []
heapq.heapify(p)

for i in range(m):

    for j in kouho[i]:
        heapq.heappush(p, j)
    if p:
        ans -= heapq.heappop(p)
print(ans)
