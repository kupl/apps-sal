import sys
from heapq import heappop, heappush

input = sys.stdin.readline


def main():
    MAX_A = 10 ** 5
    N, M = list(map(int, input().split()))
    AB = [[] for _ in range(MAX_A + 1)]
    for i in range(N):
        A, B = list(map(int, input().split()))
        AB[A].append(-B)

    p_queue = []
    ans = 0
    for m in range(1, M + 1):
        for b in AB[m]:
            heappush(p_queue, b)
        if p_queue:
            x = heappop(p_queue)
            x *= -1
            ans += x

    print(ans)


def __starting_point():
    main()

__starting_point()
