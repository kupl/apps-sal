n, m = list(map(int, input().split()))
sz = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]
l = []
dp = [0] * (n + 1)
l = list(map(int, input().split()))
l.sort(reverse=True)
dp[0] = 1
for i in range(1, n + 1):
    for j in l:
        if i - sz[j] >= 0 and dp[i - sz[j]] > 0:
            dp[i] = max(dp[i], 1 + dp[i - sz[j]])
# print(dp)
ans = []
# using the dp table construct the number
cur = n
while cur > 0:  # cur denotes count of available match sticks
 #   print(cur)
    for j in l:
        if cur - sz[j] >= 0:
            if dp[cur] == 1 + dp[cur - sz[j]] and dp[cur - sz[j]] > 0:
                ans.append(j)
                cur -= sz[j]
                break
ans.sort(reverse=True)
print((''.join(map(str, ans))))
