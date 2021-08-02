h = [list(map(int, input().split())) for _ in range(10)]

tp = {}


def celli(x, y):
    if x % 2:
        return (9 - x) * 10 + y
    return (9 - x) * 10 + 9 - y


for i in range(10):
    for j in range(10):
        if h[i][j]:
            tp[celli(i, j)] = celli(i - h[i][j], j)

dp = [0] * 94 + [6] * 5 + [0]

for i in range(93, -1, -1):
    tot = 0
    for j in range(1, 7):
        if i + j in tp:
            tot += min(dp[i + j], dp[tp[i + j]])
        else:
            tot += dp[i + j]

    tot /= 6
    tot += 1

    dp[i] = tot

print(dp[0])
