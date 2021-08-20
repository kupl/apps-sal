import itertools
K = int(input())
dp = [[0, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
lunlun_cnt = [9]
i = 1
while True:
    dp.append([0] * 10)
    lunlun_cnt_tmp = 0
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i - 1][j] + dp[i - 1][j + 1]
        elif j == 9:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j] + dp[i - 1][j + 1]
        lunlun_cnt_tmp += dp[i][j]
    i += 1
    if lunlun_cnt[-1] + lunlun_cnt_tmp >= K:
        break
    else:
        lunlun_cnt.append(lunlun_cnt[-1] + lunlun_cnt_tmp)
if K <= 9:
    pos = K
    digit = 0
else:
    pos = K - lunlun_cnt[-1]
    digit = len(lunlun_cnt)
cnt = 0
flag = False
keta = [-1, 0, 1]
for i in range(9):
    for keta_shift in itertools.product(keta, repeat=digit):
        flag2 = False
        r = i + 1
        for j in range(digit):
            r += keta_shift[j]
            if r < 0 or r > 9:
                flag2 = True
                break
        if flag2:
            continue
        cnt += 1
        if cnt == pos:
            flag = True
            break
    if flag:
        break
res = [i + 1]
for i in range(digit):
    res.append(res[-1] + keta_shift[i])
print(''.join(list(map(str, res))))
