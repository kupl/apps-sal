import sys
import heapq

input = sys.stdin.readline


def main():
    N = int(input())
    A = list(map(int, input().split()))
    heapq.heapify(A)
    while True:
        m1 = heapq.heappop(A)
        try:
            m2 = heapq.heappop(A)
        except IndexError:
            print(m1)
            break
        m2 %= m1
        heapq.heappush(A, m1)
        if m2 > 0:
            heapq.heappush(A, m2)


def __starting_point():
    main()

__starting_point()
