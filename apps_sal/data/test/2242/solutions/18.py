S = input()
dp = [0] * (len(S) + 1)
cur = int(S[len(S) - 1])
mod_10 = 1
count_num = [0] * 2019
count_num[0] += 1
for i in range(len(S)):
    dp[len(S) - i - 1] = cur
    count_num[cur] += 1
    mod_10 = mod_10 * 10 % 2019
    if i <= len(S) - 2:
        cur = (cur + int(S[len(S) - i - 2]) * mod_10) % 2019
ans = 0
for i in range(2019):
    ans += count_num[i] * (count_num[i] - 1) // 2
print(ans)
