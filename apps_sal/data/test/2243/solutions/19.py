import heapq

n, k, q = [int(x) for x in input().split()]
t = [int(x) for x in input().split()]

heap = []
for i in range(q):
    query_type, query_id = [int(x) for x in input().split()]
    if query_type == 1:
        if len(heap) < k or t[query_id - 1] > heap[0]:
            if len(heap) == k:
                heapq.heappop(heap)
            heapq.heappush(heap, t[query_id - 1])
    else:
        print('YES' if t[query_id - 1] in heap else 'NO')

