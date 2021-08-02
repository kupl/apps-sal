import heapq
n = int(input())
A = list(map(int, input().split()))
hq = []
for i in range(n):
    heapq.heappush(hq, (A[i], i))
while len(hq) >= 2:
    t1 = heapq.heappop(hq)
    t2 = heapq.heappop(hq)
    if t1[0] == t2[0]:
        A[t1[1]] = 0
        A[t2[1]] = 2 * t1[0]
        heapq.heappush(hq, (2 * t2[0], t2[1]))
    else:
        heapq.heappush(hq, t2)
print(len(A) - A.count(0))
for a in A:
    if a != 0:
        print(a, end=' ')
