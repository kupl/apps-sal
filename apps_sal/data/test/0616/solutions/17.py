def solve():
    ans = 0
    N, M = map(int, input().split())
    A, C = [0] * M, [0] * M
    for i in range(M):
        A[i], b = map(int, input().split())
        c = list(map(int, input().split()))
        for j in range(b):
            C[i] += 1 << (c[j] - 1)
    dp = [float('inf')] * (1 << N)
    dp[0] = 0
    for i in range(1, (1 << N) + 1):
        for key in range(M):
            if C[key] & i == 0:
                continue
            dp[i] = min(dp[i], dp[i & ~C[key]] + A[key])
    ans = dp[-1]
    if ans == float('inf'):
        return -1
    return ans


print(solve())
