from heapq import heapify, heappush, heappop

n, m = list(map(int, input().split()))
A = list(map(int, input().split()))

A = list([x * (-1) for x in A])

heapify(A)
for i in range(m):
    x = heappop(A)
    x = (x + 1) // 2
    heappush(A, x)

print((-1 * sum(A)))

