def d_no_need(N, K, A):
    from bisect import bisect_left
    A.sort()
    a_sorted = A[:bisect_left(A, K)]
    ans = len(a_sorted)

    dp = [False] * K
    dp[0] = True
    current_max = 0
    for idx, a in reversed(list(enumerate(a_sorted))):
        if current_max + a >= K:
            ans = idx

        updated = True
        for j in range(min(current_max, K - a - 1), -1, -1):
            if dp[j]:
                dp[j + a] = True
                if updated:
                    current_max = max(current_max, j + a)
                    updated = False
    return ans


N, K = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
print((d_no_need(N, K, A)))
