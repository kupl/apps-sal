import heapq

q = int(input())

minheap = []  # right
maxheap = []  # left
heapq.heapify(minheap)
heapq.heapify(maxheap)

s = 0
m = 0

for _ in range(0, q):
    token = input().split()
    if len(token) > 1:
        a = int(token[1])
        b = int(token[2])
        s += b
        heapq.heappush(minheap, a)
        heapq.heappush(maxheap, -a)
        if -maxheap[0] > minheap[0]:
            maxv = -heapq.heappop(maxheap)
            minv = heapq.heappop(minheap)
            m += abs(maxv - minv)
            heapq.heappush(minheap, maxv)
            heapq.heappush(maxheap, -minv)
    else:
        print(('{} {}'.format(-maxheap[0], s + m)))
