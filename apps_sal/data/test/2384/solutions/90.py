from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))
DP = defaultdict(lambda: -10 ** 18)
DP[0, 0] = A[0]
for i in range(1, N):
    for j in range((i + 1) // 2 - 1, (i + 2) // 2):
        if j == 0:
            DP[i, 0] = max(DP[i - 1, 0], A[i])
        else:
            DP[i, j] = max(DP[i - 1, j], DP[i - 2, j - 1] + A[i])
print(DP[N - 1, N // 2 - 1])
