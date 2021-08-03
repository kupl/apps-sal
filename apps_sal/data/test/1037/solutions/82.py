n = int(input())
a = list(map(int, input().split()))

a = list(enumerate(a))
a.sort(key=lambda x: x[1])

DP = [[0 for i in range(n + 1)] for j in range(n + 1)]
DP[0][0] = 0
for i in range(1, n + 1):
    pos, val = a.pop()
    pos = pos + 1

    DP[0][i] = DP[0][i - 1] + abs(val * (n - i + 1 - pos))
    DP[i][0] = DP[i - 1][0] + abs(val * (pos - i))
    for x in range(1, i):
        y = i - x
        DP[x][y] = max(DP[x - 1][y] + abs(val * (pos - x)),
                       DP[x][y - 1] + abs(val * (n - y + 1 - pos)))

ans = 0
for i in range(n + 1):
    ans = max(ans, DP[i][n - i])

print(ans)
