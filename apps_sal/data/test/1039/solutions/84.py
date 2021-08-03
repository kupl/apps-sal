import heapq
n = int(input())
g = [[] for _ in range(n)]
for i in range(n - 1):
    a, b, c = map(int, input().split())
    g[a - 1].append((b - 1, c))
    g[b - 1].append((a - 1, c))

q, k = map(int, input().split())
ds = [-1] * n
hq = [(0, k - 1)]
while hq:
    c, idx = heapq.heappop(hq)
    if ds[idx] != -1:
        continue
    ds[idx] = c
    for i in g[idx]:
        if ds[i[0]] == -1:
            heapq.heappush(hq, (i[1] + c, i[0]))

for i in range(q):
    x, y = map(int, input().split())
    print(ds[x - 1] + ds[y - 1])
