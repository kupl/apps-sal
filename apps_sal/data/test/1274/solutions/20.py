import heapq

n, m = map(int, input().split())
A = [[] for _ in range(m)]
ans = 0

for i in range(n):
    a, b = map(int, input().split())
    if m - a < 0:
        continue
    else:
        A[m - a].append(b)

available = []

for i in range(m - 1, -1, -1):
    for item in A[i]:
        heapq.heappush(available, -item)
    if available:
        ans += -heapq.heappop(available)

print(ans)
