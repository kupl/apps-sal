import heapq
N = int(input())
links = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b, c = map(int, input().split())
    links[a].append([b, c])
    links[b].append([a, c])

Q, K = map(int, input().split())

length = [-1] * (N + 1)
length[K] = 0

q = [[tmp[1], tmp[0], K] for tmp in links[K]]
heapq.heapify(q)
while q:
    tmp = heapq.heappop(q)
    length[tmp[1]] = tmp[0] + 0
    for x in links[tmp[1]]:
        if tmp[2] != x[0]:
            heapq.heappush(q, [tmp[0] + x[1], x[0], tmp[1]])

for _ in range(Q):
    x, y = map(int, input().split())
    print(length[x] + length[y])
