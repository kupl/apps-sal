import heapq
N, K = [int(x) for x in input().split()]
h = [[] for i in range(200000)]
for i in range(N):
    l, r = [int(x) for x in input().split()]
    h[l - 1].append([-(r - 1), i + 1])
g = []
t = []
heapq.heapify(t)
hist = [0] * 200000
exited = 0
for l in range(200000):
    for ri in h[l]:
        heapq.heappush(t, ri)
        hist[-ri[0]] += 1
    while len(t) - exited > K:
        top = heapq.heappop(t)
        hist[-top[0]] -= 1
        g.append(top[1])
    exited += hist[l]
print(len(g))
print(*g)
