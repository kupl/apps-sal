import heapq
import math

N, M = list(map(int, input().split()))
A = list(map(int, input().split()))


def __starting_point():
    a = [-1 * i for i in A]
    heapq.heapify(a)

    for _ in range(M):
        # pop
        temp = heapq.heappop(a)
        # push
        heapq.heappush(a, math.ceil(temp / 2))

    ans = [-1 * i for i in a]
    print((sum(ans)))


__starting_point()
