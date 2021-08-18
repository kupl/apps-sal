inf = 10000
n, s, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(input())
for i in range(n):
    if b[i] == 'R':
        b[i] = 0
    elif b[i] == 'G':
        b[i] = 1
    else:
        b[i] = 2
boxes = [[a[i], b[i], i] for i in range(n)]
boxes.sort()
l = boxes[-1][0] * n + 1
s -= 1
dp = [[[inf, s, -1] for j in range(l)] for i in range(3)]
if l < k:
    print(-1)
    return
dp[0][0][0] = 0
dp[1][0][0] = 0
dp[2][0][0] = 0
for i in range(n):
    pos = boxes[i][2]
    clr = boxes[i][1]
    cnt = boxes[i][0]
    for j in range(l - cnt):
        for c in range(3):
            if c == clr:
                continue
            if dp[clr][j + cnt][0] > dp[c][j][0] + abs(dp[c][j][1] - pos) and cnt > dp[c][j][2]:
                dp[clr][j + cnt][0] = dp[c][j][0] + abs(dp[c][j][1] - pos)
                dp[clr][j + cnt][1] = pos
                dp[clr][j + cnt][2] = cnt
ans = min(dp[0][k][0], min(dp[1][k][0], dp[2][k][0]))
for i in range(k, l):
    ans = min(min(ans, dp[0][i][0]), min(dp[1][i][0], dp[2][i][0]))
if ans < inf:
    print(ans)
else:
    print(-1)
