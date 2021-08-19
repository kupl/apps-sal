from heapq import heapify, heappush, heappop
N = int(input())
A = []
for i in range(N):
    A.append(tuple(map(int, input().split())))
A.sort()
B = []
for i in range(N):
    B.append(tuple(map(int, input().split())))
B.sort()
heap = []
heapify(heap)
aindex = count = 0
for b in B:
    while aindex < len(A) and A[aindex][0] < b[0]:
        heappush(heap, -A[aindex][1])
        aindex += 1
    buf = []
    while heap and b[1] <= -heap[0]:
        ay = heappop(heap)
        buf.append(ay)
    if heap and -heap[0] < b[1]:
        count += 1
        heappop(heap)
    for ay_ in buf:
        heappush(heap, ay_)
print(count)
