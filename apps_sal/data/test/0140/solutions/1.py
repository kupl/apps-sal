import sys
from operator import itemgetter
input = sys.stdin.readline
(n, m) = map(int, input().split())
info = [list(map(int, input().split())) for i in range(n)]
INF = 10 ** 9
new_info = []
for (pos, width) in info:
    tmp = [max(pos - width - 1, 0), min(pos + width, m)]
    new_info.append(tmp)
pos = 0
new_info = sorted(new_info, key=itemgetter(1))
dp = [[0] * (m + 2) for i in range(n + 1)]
for i in range(m + 2):
    dp[0][i] = i
for i in range(n):
    (begin, end) = new_info[i]
    for j in range(m + 2):
        if j <= end:
            dp[i + 1][j] = min(dp[i][begin], dp[i][j])
        else:
            dp[i + 1][j] = min(j - end + dp[i][max(begin - (j - end), 0)], dp[i][j])
print(dp[n][m])
