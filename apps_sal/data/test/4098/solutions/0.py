import bisect

n, k = list(map(int, input().split()))
A = list(map(int, input().split()))
A.sort()

DP = [[0] * (k + 1) for i in range(n)]

for i in range(n):
    x = bisect.bisect_right(A, A[i] + 5) - 1
    for j in range(k - 1, -1, -1):
        DP[i][j] = max(DP[i][j], DP[i - 1][j])
        DP[x][j + 1] = max(DP[i - 1][j] + x - i + 1, DP[x][j + 1])

print(max([DP[i][-1] for i in range(n)]))
