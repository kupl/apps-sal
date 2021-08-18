import heapq

heap = []

n = int(input())

V = list(map(int, input().split()))

T = list(map(int, input().split()))

tmp = 0

for i in range(n):

    ans = 0

    heapq.heappush(heap, tmp + V[i])

    while len(heap) and heap[0] <= tmp + T[i]:

        ans += heapq.heappop(heap) - tmp

    tmp += T[i]

    ans += T[i] * len(heap)

    print(ans, end=' ')
