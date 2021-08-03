n = int(input())
a = list(map(int, input().split()))
dp = [0] * (max(a) + 1)
a.sort()

for i in a:
    temp = i
    while temp <= a[-1]:
        dp[temp] += 1
        temp += i
ans = 0
for i in a:
    if dp[i] == 1:
        ans += 1

print(ans)
