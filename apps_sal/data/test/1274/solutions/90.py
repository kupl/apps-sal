import heapq
(N, M) = map(int, input().split())
arubaito = [list(map(int, input().split())) for _ in range(N)]
arubaito.sort()
arubaito2 = [[] for _ in range(M + 1)]
for i in range(N):
    if arubaito[i][0] <= M:
        arubaito2[arubaito[i][0]].append(arubaito[i][1])
for i in range(M):
    arubaito2[i].sort(reverse=True)
target = []
ans = 0
heapq.heapify(target)
for i in range(1, M + 1):
    for k in arubaito2[i]:
        heapq.heappush(target, k * -1)
    if len(target) > 0:
        ans += heapq.heappop(target) * -1
print(ans)
