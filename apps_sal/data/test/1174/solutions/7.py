import heapq
import sys


def input():
    return sys.stdin.readline().rstrip()


(N, M) = list(map(int, input().split()))
A = list([int(x) * -1 for x in input().split()])
heapq.heapify(A)
for i in range(M):
    a = heapq.heappop(A)
    a *= -1
    a //= 2
    a *= -1
    heapq.heappush(A, a)
print(-sum(A))
