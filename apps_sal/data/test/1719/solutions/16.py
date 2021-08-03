N = int(input())
dp = [[0] * 64 for i in range(N - 2)]
# 3進数で管理
mod = 10**9 + 7

d = dict()
d2 = dict()
d2[0] = 'A'
d2[1] = 'G'
d2[2] = 'C'
d2[3] = 'T'
for i in range(64):
    k = i
    ret = ''
    for j in range(3):
        ret += d2[k % 4]
        k //= 4
    d[i] = ret


for i in range(64):
    if d[i] == 'AGC' or d[i] == 'GAC' or d[i] == "ACG":
        continue

    else:
        dp[0][i] = 1


for i in range(N - 3):
    for j in range(64):
        if dp[i][j] == 0:
            continue
        tmp = j // 4
        for k in range(4):
            idx = tmp + k * 16
            if d[idx] == "AGC" or d[idx] == 'ACG' or d[idx] == "GAC" or (d[j][0] == 'A' and d[j][1] == 'G' and k == 2) or (d[j][0] == 'A' and d[j][2] == 'G' and k == 2):
                #print(d[j] + d2[k])
                continue
            dp[i + 1][idx] += dp[i][j]


print((sum(dp[-1]) % mod))
