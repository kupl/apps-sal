n = int(input())
mod = 10**9 + 7
dp = [[0] * (4**3) for i in range(n)]
dic = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
agct_to_num = dict()
num_to_agct = dict()
for i in 'AGCT':
    for j in 'AGCT':
        for k in 'AGCT':
            num = dic[i] * 16 + dic[j] * 4 + dic[k] * 1
            agct_to_num[i + j + k] = num
            num_to_agct[num] = i + j + k

dp[0] = [1] * (4**3)
dp[1] = [1] * (4**3)
dp[2] = [1] * (4**3)
dp[2][agct_to_num['AGC']] = 0
dp[2][agct_to_num['ACG']] = 0
dp[2][agct_to_num['GAC']] = 0


def is_ok(s):
    if 'AGC' in s:
        return False
    for i in range(len(s) - 1):
        t = list(s)
        t[i], t[i + 1] = t[i + 1], t[i]
        if 'AGC' in ''.join(t):
            return False
    return True


for i in range(3, n):
    for j in range(64):
        for c in 'ACGT':
            tmp = num_to_agct[j] + c
            if is_ok(tmp):
                dp[i][agct_to_num[tmp[1:]]] += dp[i - 1][j]

print(sum(dp[n - 1]) % mod)
