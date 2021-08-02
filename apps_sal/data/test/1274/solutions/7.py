import heapq
N, M = map(int, input().split())

jobs = [[] for _ in range(M)]
for _ in range(N):
    A, B = map(int, input().split())
    if A > M:
        continue
    jobs[A - 1].append(-B)

total = 0
heap = []
for i in range(M):
    for job in jobs[i]:
        heapq.heappush(heap, job)

    if len(heap) == 0:
        continue
    else:
        total += -heapq.heappop(heap)

print(total)
