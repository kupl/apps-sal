def f_select_half():
    from collections import defaultdict
    N = int(input())
    A = [int(i) for i in input().split()]

    dp = defaultdict(lambda: -float('inf'))
    dp[(0, 0, 0)] = 0

    for k, a in enumerate(A, 1):
        j = k // 2
        for x in range(j - 1, j + 2):
            dp[(k, x, 0)] = max(dp[(k - 1, x, 0)], dp[k - 1, x, 1])
            dp[(k, x, 1)] = dp[(k - 1, x - 1, 0)] + a
    return max(dp[(N, N // 2, f)] for f in (0, 1))


print(f_select_half())
