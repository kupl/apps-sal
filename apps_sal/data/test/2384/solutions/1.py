import sys
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
A = [int(i) for i in input().split()]
inf = float("inf")
DP = [[-inf] * 4 for _ in range(n + 1)]
DP[0][2] = 0
for i, a in enumerate(A):
    if (i + 1) % 2 == 0:
        DP[i + 1][0] = DP[i][3] + a
        if i >= 1:
            DP[i + 1][0] = max(DP[i + 1][0], DP[i - 1][2] + a)
        DP[i + 1][2] = DP[i][0]
        DP[i + 1][3] = max(DP[i][1], DP[i][3])
        if i >= 1:
            DP[i + 1][3] = max(DP[i + 1][3], DP[i - 1][2])
    else:
        DP[i + 1][0] = DP[i][2] + a
        DP[i + 1][1] = DP[i][3] + a
        DP[i + 1][3] = max(DP[i][0], DP[i][2])
if n % 2 == 0:
    print((max(DP[n][0], DP[n][2])))
else:
    print((max(DP[n][1], DP[n][3])))
