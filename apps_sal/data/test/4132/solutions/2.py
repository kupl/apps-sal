import heapq

n = int(input())
A = [int(a) for a in input().split()]

heapq.heapify(A)

while True:
    temp = heapq.heappop(A)
    A = [a%temp for a in A if a % temp != 0] + [temp]
    if len(A) == 1:
        break

print(A[0])
