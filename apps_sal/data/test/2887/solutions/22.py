import heapq as hq
n = int(input())
heap = []
temp = 0
ans = [-1 for _ in range(n)]
V = [int(x) for x in input().split()]
T = [int(x) for x in input().split()]
for i in range(n):
    prevtemp = temp
    temp += T[i]
    hq.heappush(heap, V[i] + prevtemp)
    curr = 0
    while len(heap) and heap[0] <= temp:
        m = hq.heappop(heap)
        curr += m - prevtemp
    curr += len(heap) * T[i]
    ans[i] = curr
print(' '.join([str(x) for x in ans]))
