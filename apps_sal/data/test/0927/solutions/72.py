def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    from collections import Counter, deque
    #from collections import defaultdict
    from itertools import combinations, permutations, accumulate, groupby
    #from itertools import product
    from bisect import bisect_left, bisect_right
    from heapq import heapify, heappop, heappush
    from math import floor, ceil
    #from operator import itemgetter

    #inf = 10**17
    #mod = 10**9 + 7

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    # 使う本数の種類
    b = set()
    matti = [2, 5, 5, 4, 5, 6, 3, 7, 6]
    for i in a:
        b.add(matti[i - 1])

    dp = [-1] * (n + 1)
    dp[0] = 0
    for i in range(n + 1):
        for j in b:
            if i >= j:
                dp[i] = max(dp[i - j] + 1, dp[i])

    keta = dp[-1]
    res = []
    a.sort(reverse=True)
    cnt = n
    while cnt > 0:
        for i in a:
            if cnt >= matti[i - 1]:
                if dp[cnt] - dp[cnt - matti[i - 1]] == 1:
                    res.append(str(i))
                    cnt -= matti[i - 1]
                    break
    print(''.join(res))


def __starting_point():
    main()


__starting_point()
