n = int(input())
C = [int(i) for i in input().split()]

D = []
for c in C:
    if not D or D[-1] != c:
        D.append(c)

n = len(D)
C = D[::-1]
DP = [[0] * (n + 1) for i in range(n + 1)]

for i in range(n):
    for j in range(n):
        if C[i] == D[j]:
            DP[i + 1][j + 1] = DP[i][j] + 1
        else:
            DP[i + 1][j + 1] = max(DP[i + 1][j], DP[i][j + 1])

print(n - 1 - DP[n][n] // 2)
