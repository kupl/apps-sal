import heapq
(N, M) = list(map(int, input().split()))
AB = [list(map(int, input().split())) for _ in range(N)]
AB = sorted(AB, key=lambda x: x[0])
x = 0
res = 0
hq = []
heapq.heapify(hq)
for i in range(M):
    for j in range(x, N):
        if AB[j][0] > i + 1:
            x = j
            break
        heapq.heappush(hq, AB[j][1] * -1)
    else:
        x = N
    if hq:
        res += heapq.heappop(hq) * -1
print(res)
