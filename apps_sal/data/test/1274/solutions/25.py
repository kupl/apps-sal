from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right


def main():
    N, M = list(map(int, input().split()))
    AB = [[] for _ in range(10**5)]
    for i in range(N):
        a, b = list(map(int, input().split()))
        AB[a - 1].append(b)

    q = []
    ans = 0
    i = 0
    while i < M:
        for ab in AB[i]:
            heappush(q, -ab)
        if q:
            ans -= heappop(q)
        i += 1
    print(ans)


def __starting_point():
    main()


__starting_point()
