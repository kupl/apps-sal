import heapq
(n, m) = list(map(int, input().split()))
ab = [[] for i in range(10 ** 5)]
for i in range(n):
    (a, b) = list(map(int, input().split()))
    ab[a - 1].append(b * -1)
que = []
ans = 0
for i in range(m):
    for b in ab[i]:
        heapq.heappush(que, b)
    if que:
        ans += heapq.heappop(que)
print(ans * -1)
