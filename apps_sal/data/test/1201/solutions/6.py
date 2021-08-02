from sys import stdin
input = stdin.readline
n = int(input())
T = 2001
t, d, p, idx = [], [], [], []
ans = []
arr = []
for i in range(n):
    a, b, c = map(int, input().split())
    arr.append([a, b, c, i])
arr.sort(key=lambda x: x[1])
for i in arr:
    t.append(i[0]); d.append(i[1]); p.append(i[2]); idx.append(i[3])
dp = [[0 for j in range(n)] for i in range(T)]
for time in range(1, T):
    for i in range(n):
        #dp[time][i] = max(dp[time - 1][i], dp[time][i - 1])
        dp[time][i] = dp[time][i - 1]
        if d[i] > time >= t[i]:
            if i:
                dp[time][i] = max(dp[time][i], p[i] + dp[time - t[i]][i - 1])
            else:
                dp[time][i] = p[i]
b = [0, [0, 0]]
for i in range(T):
    for j in range(n):
        if b[0] < dp[i][j]:
            b = [dp[i][j], [i, j]]
print(b[0])
b = b[1]
while dp[b[0]][b[1]] and b[0] > -1:
    if b[1] and dp[b[0]][b[1]] != dp[b[0]][b[1] - 1]:
        ans.append(b[1])
        b[0] -= t[b[1]]
    elif b[1] == 0:
        if dp[b[0]][b[1]]:
            ans.append(b[1])
        break
    b[1] -= 1
print(len(ans))
for i in ans[::-1]:
    print(idx[i] + 1, end=' ')
