(n, m) = map(int, input().split())
num = {1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}
a = list(map(int, input().split()))
a.sort(reverse=True)
dp = [0] + [-1] * (n + 1)
for i in range(n):
    for j in a:
        if i + num[j] <= n:
            dp[i + num[j]] = max(dp[i + num[j]], dp[i] + 1)
ans = []
match = n
while match > 0:
    for i in a:
        if match - num[i] >= 0 and dp[match - num[i]] == dp[match] - 1:
            match -= num[i]
            ans.append(str(i))
            break
print(''.join(ans))
