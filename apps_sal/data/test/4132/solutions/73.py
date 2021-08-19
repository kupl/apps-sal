from heapq import heappop, heappush
N = int(input())
A = list(map(lambda x: -1 * int(x), input().split()))
now = -1 * heappop(A)
while A:
    next = -1 * heappop(A)
    if now % next != 0:
        heappush(A, -1 * (now % next))
    now = next
print(now)
