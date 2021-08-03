from math import inf as inf
import sys
for _ in range(int(input())):
    n = int(sys.stdin.readline())
    dp = [[inf, inf, inf] for _ in range(n + 1)]
    arr = []
    for i in range(n):
        arr.append(list(map(int, sys.stdin.readline().split())))
    dp[0] = [0, arr[0][1], arr[0][1] * 2]

    for i in range(1, n):
        for j in range(3):
            for k in range(3):
                if arr[i][0] + j != arr[i - 1][0] + k:
                    dp[i][j] = min(dp[i][j], dp[i - 1][k] + j * arr[i][1])
    print(min(dp[n - 1]))
