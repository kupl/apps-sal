from heapq import heappop, heappush, heapify
import sys
input = sys.stdin.readline
n = int(input())
(b, _) = list(map(int, input().split()))
heap = []
heap2 = []
for _ in range(n - 1):
    (t, w) = list(map(int, input().split()))
    if t > b:
        heap.append(w + 1 - t)
    else:
        heap2.append((-t, -w))
heapify(heap)
heapify(heap2)
ans = len(heap) + 1
while heap:
    need = heap[0]
    if need > b:
        break
    b -= need
    heappop(heap)
    while heap2 and -heap2[0][0] > b:
        (t, w) = heappop(heap2)
        (t, w) = (-t, -w)
        heappush(heap, w + 1 - t)
    cur = len(heap) + 1
    ans = min(ans, cur)
print(ans)
