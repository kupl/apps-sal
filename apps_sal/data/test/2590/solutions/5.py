import bisect
import collections
import heapq


def solution():
    n, xVal = [int(x) for x in input().strip().split()]
    a = [int(x) for x in input().strip().split()]

    curSum = sum(a)
    heapq.heapify(a)
    while a and curSum / len(a) < xVal:
        curSum -= heapq.heappop(a)
    print(len(a))


def main():
    T = int(input().strip())
    for _ in range(T):
        solution()


def __starting_point():
    main()


__starting_point()
