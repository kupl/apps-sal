s = input()
l, n = [], len(s)
i = 0
while i < n:
    j = i
    while j < n and s[j] == 'v':
        j += 1
    l.append(max(j - i - 1, 0))
    i = j
    while j < n and s[j] == 'o':
        j += 1
    l.append(j - i)
    i = j
dp = [0, 0, 0]
for i in range(len(l)):
    if i & 1:
        dp[1] += dp[0] * l[i]
    else:
        dp[2] += dp[1] * l[i]
        dp[0] += l[i]
# print(*l)
print(dp[-1])
