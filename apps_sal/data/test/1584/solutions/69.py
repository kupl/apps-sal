import sys
from bisect import bisect_left

input = sys.stdin.readline


def main():
    N = int(input())
    L = list(map(int, input().split()))

    L.sort()
    ans = 0
    for a in range(N - 2):
        for b in range(a + 1, N - 1):
            x = bisect_left(L, L[a] + L[b])
            ans += (x - 1 - b)

    print(ans)


def __starting_point():
    main()

__starting_point()
