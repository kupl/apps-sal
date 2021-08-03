input_string = input().split()
n = int(input_string[0])
l = int(input_string[1])
input_string = input().split()
v = []
for i in range(0, len(input_string)):
    v.append(int(input_string[i]))
dp = [0]
for i in range(1, len(v) + 1):
    dp.append(dp[i - 1] + v[i - 1])
ans = 1000000000000000000000000000
for i in range(l, len(dp)):
    ans = min(ans, dp[i] - dp[i - l])
print(ans)
