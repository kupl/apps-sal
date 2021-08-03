N = int(input())
A = [int(input()) for _ in range(N)]


def solve(A, n):
    import bisect
    dp = [float('inf')] * n
    for i in range(n - 1, -1, -1):
        k = bisect.bisect_right(dp, A[i])
        dp[k] = A[i]
    ans = 0
    for a in dp:
        if a != float('inf'):
            ans += 1
        else:
            break
    return ans


print(solve(A, N))
