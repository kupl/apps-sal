import heapq

n, k, qs = list(map(int, input().split()))
arr = [int(i) for i in input().split()]
d = []
for i in range(qs):
    q, ind = list(map(int, input().split()))
    if q == 1:
        heapq.heappush(d, (arr[ind-1], ind))
    if len(d) > k:
        heapq.heappop(d)
    if q == 2:
        if (arr[ind-1], ind) in d: print("YES")
        else: print("NO")

