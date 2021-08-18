import sys
import math
from collections import deque
from collections import defaultdict
INF = 10**9


def main():
    h, n = list(map(int, sys.stdin.readline().split()))
    magic = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    max_a = max(a for a, b in magic)
    dp = [0] * (h + max_a + 1)
    for i in range(1, h + max_a):
        dp[i] = min(dp[i - a] + b for a, b in magic)
    print(dp[h])

    return 0


def __starting_point():
    main()


__starting_point()
