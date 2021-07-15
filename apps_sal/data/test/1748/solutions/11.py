from sys import stdin, stdout
import heapq

n = int(input())
v = list(map(int, input().split()))
t = list(map(int, input().split()))

heap = []
sum = 0
for i in range(n):
    ans = 0
    heapq.heappush(heap, sum + v[i])
    while len(heap) and heap[0] <= sum + t[i]:
        ans += heap[0] - sum
        heapq.heappop(heap)
    ans += len(heap) * t[i]
    sum += t[i]
    print(ans, end=' ')
