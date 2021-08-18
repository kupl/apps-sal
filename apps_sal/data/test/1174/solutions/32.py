import heapq

N, M = list(map(int, input().split()))
A = list([int(x) * (-1) for x in input().split()])


heapq.heapify(A)
for i in range(M):
    max_num = heapq.heappop(A) * (-1)
    heapq.heappush(A, (-1) * (max_num // 2))

A = [x * (-1) for x in A]
print((sum(A)))
