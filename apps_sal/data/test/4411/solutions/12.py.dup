import heapq

N, K = [int(x) for x in input().split()]
L2RI = [[] for i in range(200000)]
for i in range(N):
    l, r = [int(x) for x in input().split()]
    L2RI[l - 1].append([-(r - 1), i + 1])

ans = []
que = []
heapq.heapify(que)

hist = [0] * 200000
exited = 0

for l in range(200000):
    for ri in L2RI[l]:
        heapq.heappush(que, ri)
        hist[-ri[0]] += 1
    while len(que) - exited > K:
        top = heapq.heappop(que)
        hist[-top[0]] -= 1
        ans.append(top[1])
    exited += hist[l]

print(len(ans))
print(*ans)
