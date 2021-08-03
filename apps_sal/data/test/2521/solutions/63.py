import sys
from heapq import *
input = sys.stdin.readline


def main():
    n = int(input())
    a = list(map(int, input().split()))

    af = a[:n]
    ab = [-v for v in a[2 * n:]]
    af_sum = sum(af)
    ab_sum = -sum(ab)

    heapify(af)
    heapify(ab)
    judge = [0] * (n + 1)
    judge[0] += af_sum
    judge[n] -= ab_sum

    for i in range(n):
        if a[n + i] > af[0]:
            af_sum -= heappop(af)
            heappush(af, a[n + i])
            af_sum += a[n + i]
        judge[i + 1] += af_sum

        if -a[2 * n - 1 - i] > ab[0]:
            ab_sum += heappop(ab)
            heappush(ab, -a[2 * n - 1 - i])
            ab_sum += a[2 * n - 1 - i]
        judge[n - 1 - i] -= ab_sum

    ans = max(judge)
    print(ans)


def __starting_point():
    main()


__starting_point()
