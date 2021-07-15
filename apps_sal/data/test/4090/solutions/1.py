# import time
N = 303
eq = []
dp = []
for i in range(N):
    eq.append([False] * N)
for i in range(N):
    dp.append([0] * N)
n = int(input())
s = input()
# t = time.time()
allsum = len(s)
s = s.split()
for i in range(n):
    eq[i][i] = True
    for j in range(i):
        eq[i][j] = eq[j][i] = s[i] == s[j]
for i in range(n - 1, -1, -1):
    for j in range(n - 1, -1, -1):
        if eq[i][j]:
            if i < n - 1 and j < n - 1:
                dp[i][j] = dp[i + 1][j + 1] + 1
            else:
                dp[i][j] = 1
ans = allsum
for i in range(n):
    su = 0
    for j in range(n - i):
        su += len(s[i + j])
        cnt = 1
        pos = i + j + 1
        while pos < n:
            if dp[i][pos] > j:
                cnt += 1
                pos += j
            pos += 1
        cur = allsum - su * cnt + (j + 1) * cnt - j * cnt
        if cnt > 1 and ans > cur:
            # print(allsum, su, cnt, j)
            ans = cur
print(ans)
# print(time.time() - t)

