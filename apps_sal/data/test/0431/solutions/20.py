n,m = list(map(int, input().split()))
inf = 10 ** 10
dp = [[inf, inf] for i in range(n)]
a = []
last = -1
for i in range(n):
    tmp = input()
    tmp1 = []
    for j in range(len(tmp)):
        if tmp[j] == "1":
            tmp1.append(1)
            if last == -1:
                last = n - i - 1
        else:
            tmp1.append(0)
    a.append(tmp1)
a = a[::-1]
left = [-1] * n
right = [-1] * n
for i in range(n):
    for j in range(m + 2):
        if a[i][j] and left[i] == -1:
            left[i] = j
        if a[i][j]:
            right[i] = j
if last == -1:
    print(0)
    return
if last == 0:
    print(right[0])
    return
            
dp[0][0] = max(0, right[0] * 2)
dp[0][1] = m + 1
for i in range(1,last):
    if right[i] != - 1:
        dp[i][0] = min(dp[i][0], dp[i - 1][0] + 1 + 2 * right[i])
    else:
        dp[i][0] = min(dp[i][0], dp[i - 1][0] + 1)
    dp[i][0] = min(dp[i][0], dp[i - 1][1] + m + 2)
    if left[i] != - 1:
        dp[i][1] = min(dp[i][1], dp[i - 1][1] + 1 + (m + 1 - left[i]) * 2)
    else:
        dp[i][1] = min(dp[i][1], dp[i - 1][1] + 1)
    dp[i][1] = min(dp[i][1], dp[i - 1][0] + m + 2)
    
lf,rf = inf,inf
if right[last] != -1:
    lf = dp[last - 1][0] + 1 + right[last]
else:
    lf = dp[last - 1][0]  + 1
lf = min(lf, dp[last - 1][1] + m + 2)

if left[last] != -1:
    rf = dp[last - 1][1] + 1 + (m + 1 - left[last])
else:
    rf = dp[last - 1][1] + 1
rf = min(rf, dp[last - 1][0] + m + 2)
print(min(lf,rf))


    

