import heapq
import sys
input = sys.stdin.readline

t = int(input())
for tests in range(t):
    n, k = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = sorted(map(int, input().split()), reverse=True)

    heapq.heapify(A)

    for i in range(k):
        x = heapq.heappop(A)
        if B[i] > x:
            x = B[i]
        heapq.heappush(A, x)

    print(sum(A))
