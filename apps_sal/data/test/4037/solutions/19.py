z, r = list(map(int, input().split()))
a = []
cnt = 0
for i in range(z):
    a.append([int(j) for j in input().split()])
flag = True
while flag:
    flag = False
    for i in a:
        if r >= i[0] and i[1] >= 0:
            flag = True
            r += i[1]
            cnt += 1
            a.remove(i)
            break
a = sorted(a, key=lambda x: x[0] + x[1])
dp = [[0] * (r + 1) for i in range(len(a) + 1)]
for i in range(len(a)):
    for j in range(r + 1):
        dp[i][j] = dp[i - 1][j]
        if j >= a[i][0] and j + a[i][1] >= 0:
            dp[i][j] = max(dp[i][j], dp[i - 1][j + a[i][1]] + 1)
print(cnt + dp[len(a) - 1][r])
