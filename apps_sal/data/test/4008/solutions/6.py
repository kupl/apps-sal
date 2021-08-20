(n, k) = map(int, input().split())
a = list(map(int, input().split()))
tup = [[0, 0] for i in range(n)]
for i in range(n):
    tup[i] = [a[i], i]
tup.sort()
dp = [0] * n
dp[tup[0][1]] = 1
cp = 1
flag = 0
ct = 1
for i in range(1, n):
    if tup[i][0] == tup[i - 1][0]:
        ct = ct % k + 1
        cp += 1
        if cp > k:
            print('NO')
            flag = 1
            break
        dp[tup[i][1]] = ct
    else:
        ct = ct % k + 1
        cp = 1
        dp[tup[i][1]] = ct
if flag == 0:
    print('YES')
    for i in range(n):
        print(dp[i], end=' ')
