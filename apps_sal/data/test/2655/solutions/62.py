import heapq

N = int(input())
A = [int(x) * -1 for x in input().split()]
heapq.heapify(A)
conf = heapq.heappop(A) * -1

for i in range(N - 2):
    feel = heapq.heappop(A) * -1
    conf += feel
    if i % 2 == 0:
        heapq.heappush(A, feel * -1)

print(conf)
