l = int(input())
d = input()
sums = []
dp = [-1] * (l + 1)
dp[0] = 0
sums.append(0)
mlen = 0
for i in range(1, l + 1):
    sums.append(sums[-1] + 2 * int(d[i - 1]) - 1)
    if dp[sums[-1]] == -1:
        dp[sums[-1]] = i
    else:
        mlen = max(mlen, i - dp[sums[-1]])
print(mlen)
