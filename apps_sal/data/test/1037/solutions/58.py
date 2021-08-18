N = int(input())
A = list(map(int, input().split()))
table = []

for i, a in enumerate(A):
    table.append([a, i])
table.sort()

DP = [[0 for i in range(N + 1)] for j in range(N + 1)]
for i in range(1, N + 1):
    baby, pos = table.pop()

    DP[i][0] = DP[i - 1][0] + baby * abs(pos - i + 1)
    DP[0][i] = DP[0][i - 1] + baby * abs(pos - (N - i))
    for x in range(1, i):
        y = i - x

        DP[x][y] = max(DP[x - 1][y] + baby * abs(pos - x + 1),
                       DP[x][y - 1] + baby * abs(pos - (N - y)))

ans = 0
for i in range(N + 1):
    ans = max(ans, DP[i][N - i])
print(ans)
