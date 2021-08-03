n = int(input())
s = input()
a = list(s.split())
eq = [[0 for i in range(n)] for j in range(n)]
dp = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    eq[i][i] = 1
    for j in range(0, i):
        if a[i] == a[j]:
            eq[i][j] += 1
            eq[j][i] += 1
for i in range(n - 1, -1, -1):
    for j in range(n - 1, -1, -1):
        if eq[i][j] == 1:
            if i < n - 1 and j < n - 1:
                dp[i][j] = dp[i + 1][j + 1] + 1
            else:
                dp[i][j] = 1
allsum = n - 1
for k in a:
    allsum += len(k)
ans = allsum
for i in range(n):
    sx = 0
    j = 0
    while i + j < n:
        sx += len(a[i + j])
        cnt = 1
        pos = i + j + 1
        while pos < n:
            if dp[i][pos] > j:
                cnt += 1
                pos += j
            pos += 1
        cur = allsum - sx * cnt + (j + 1) * cnt - j * cnt
        if cnt > 1 and ans > cur:
            ans = cur
        j += 1
print(ans)
