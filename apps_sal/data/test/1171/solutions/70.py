import sys
from bisect import bisect_left


read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60


def main():
    N, K, *V = list(map(int, read().split()))

    ans = 0
    for k in range(min(N, K) + 1):
        for left in range(k + 1):
            right = k - left
            tmp = V[:left] + (V[-right:] if right else [])
            tmp.sort()

            idx = bisect_left(tmp, 0)
            if idx > K - k:
                idx = K - k

            this_ans = sum(tmp[idx:])
            if ans < this_ans:
                ans = this_ans

    print(ans)
    return


def __starting_point():
    main()

__starting_point()
