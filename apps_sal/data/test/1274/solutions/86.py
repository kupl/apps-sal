import heapq
(n, m) = list(map(int, input().split()))
ab = [[] for i in range(m + 1)]
d = []
for i in range(n):
    (a, b) = list(map(int, input().split()))
    if not a > m:
        ab[a - 1].append(-1 * b)
res = 0
cnt = 0
for i in range(m):
    for j in range(len(ab[i])):
        heapq.heappush(d, ab[i][j])
    if len(d):
        res += heapq.heappop(d)
print(-1 * res)
