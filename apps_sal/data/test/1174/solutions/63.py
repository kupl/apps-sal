import heapq

n, m = map(int, input().split())
hp = map(lambda x: (-1) * int(x), input().split())
hp = list(hp)
heapq.heapify(hp)

for i in range(m):
    item = -1 * heapq.heappop(hp)
    # print('item',item)
    item = item // 2
    heapq.heappush(hp, -item)

print(-1 * sum(hp))
