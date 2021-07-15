import sys
import math
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    N, K = list(map(int, input().split()))
    A = list(map(int, input().split()))

    d = defaultdict(int)
    for a in A:
        if a == 0:
            continue
        digit = int(math.log2(a))
        for i in range(digit + 1):
            if 1 << i & a:
                d[i] += 1

    x = 0
    if K != 0:
        digit = int(math.log2(K))
        for i in range(digit + 1)[::-1]:
            if N / 2 <= d[i]:
                continue
            else:
                if K < x + 2 ** i:
                    continue
                else:
                    x += 2 ** i

    ans = 0
    for a in A:
        ans += x ^ a

    print(ans)


def __starting_point():
    main()

__starting_point()
