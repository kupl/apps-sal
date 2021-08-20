def subsequences_of_length(s):
    n = len(s)
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    to_int = {}
    for (i, char) in enumerate(alphabet):
        to_int[char] = i
    next_i = [[n] * len(alphabet) for i in range(n + 1)]
    for i in reversed(range(n)):
        for (j, char) in enumerate(alphabet):
            next_i[i][j] = next_i[i + 1][j]
        next_i[i][to_int[s[i]]] = i
    dp = [[0] * (n + 1) for i in range(n + 1)]
    dp[0][0] = 1
    for i in range(n):
        for k in range(n):
            for j in range(26):
                if next_i[i][j] >= n:
                    continue
                dp[k + 1][next_i[i][j] + 1] += dp[k][i]
    ans = [sum(dp[i]) for i in range(n + 1)]
    return ans


(n, k) = map(int, input().split())
s = input()
ans_len = subsequences_of_length(s)
ans_cnt = 0
ans = 0
for length in reversed(range(len(ans_len))):
    cnt = ans_len[length]
    if ans_cnt + cnt <= k:
        ans_cnt += cnt
        ans += cnt * (n - length)
    else:
        ans += (k - ans_cnt) * (n - length)
        ans_cnt = k
if ans_cnt != k:
    print(-1)
else:
    print(ans)
