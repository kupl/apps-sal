def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10000000)
    from collections import Counter, deque
    #from collections import defaultdict
    from itertools import combinations, permutations
    #from itertools import accumulate, product
    from bisect import bisect_left,bisect_right
    from math import floor, ceil
    #from operator import itemgetter
    import numpy as np
    #mod = 1000000007

    N,K = map(int, input().split())
    a = list(map(int, input().split()))
    a = sorted(a)

    def check(num):
        dp = np.zeros((N+1, K), dtype=np.bool)
        dp[0,0] = 1
        for i in range(N):
            # まとめて遷移
            dp[i+1] |= dp[i]
            #i番目のカードはスルー
            if i != num and a[i] < K:
                dp[i+1,a[i]:] |= dp[i,:K-a[i]]
        return any(dp[N, -a[num]:])

    left = -1
    right = N
    while right - left > 1:
        mid = (left+right)//2
        if check(mid):
            right = mid
        else:
            left = mid
    print(right)

    # 間に合わないよ～><
    # def dp(num):
    #     dp = [[0]*(K) for _ in range(n)]
    #     dp[0][0] = 1
    #     b = a[:num]+a[num+1:] #N-1個
    #     for i in range(n-1):
    #         for j in range(K):
    #             if b[i]<=j:
    #                 dp[i+1][j] = dp[i][j-b[i]] or dp[i][j]
    #             else:
    #                 dp[i+1][j]=dp[i][j]
    #     return any(dp[n-1][K-a[num]:])

def __starting_point():
    main()
__starting_point()
