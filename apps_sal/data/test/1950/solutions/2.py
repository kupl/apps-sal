import heapq


def ip():
    return map(int, input().split())


n = ip()
l = list(ip())
if len(l) % 2 == 0:
    l.append(0)
heapq.heapify(l)
pen = 0
while len(l) > 1:
    x = heapq.heappop(l)
    y = heapq.heappop(l)
    z = heapq.heappop(l)
    pen = pen + x + y + z
    heapq.heappush(l, x + y + z)
print(pen)
