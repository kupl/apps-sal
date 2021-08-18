n = int(input())
C = [int(i) for i in input().split()]

INF = 5000
DP = [[[0] * (2) for i in range(n)] for j in range(2)]

for i in range(n - 1):
    for j in range(n - i - 1):
        DP[(i + 1) % 2][j][0] = INF
        DP[(i + 1) % 2][j][1] = INF
        for k in range(2):
            c = C[j] if k == 0 else C[j + i]
            if c == C[j + i + 1]:
                DP[(i + 1) % 2][j][1] = min(DP[(i + 1) % 2][j][1], DP[i % 2][j][k])
            else:
                DP[(i + 1) % 2][j][1] = min(DP[(i + 1) % 2][j][1], DP[i % 2][j][k] + 1)

            c = C[j + 1] if k == 0 else C[j + i + 1]
            if c == C[j]:
                DP[(i + 1) % 2][j][0] = min(DP[(i + 1) % 2][j][0], DP[i % 2][j + 1][k])
            else:
                DP[(i + 1) % 2][j][0] = min(DP[(i + 1) % 2][j][0], DP[i % 2][j + 1][k] + 1)

print(min(DP[(n - 1) % 2][0]))
