import heapq
n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))

b = a.copy()

# これを加える！！！！


def _heappush_max(heap, item):
    heap.append(item)
    heapq._siftdown_max(heap, 0, len(heap) - 1)


def _heappop_max(heap):
    """Maxheap version of a heappop."""
    lastelt = heap.pop()    # raises appropriate IndexError if heap is empty
    if heap:
        returnitem = heap[0]
        heap[0] = lastelt
        heapq._siftup_max(heap, 0)
        return returnitem
    return lastelt


b = sorted(b, reverse=True)

b1 = _heappop_max(b)
b2 = _heappop_max(b)

for i in range(n):
    if a[i] == b1:
        print(b2)
    else:
        print(b1)
