(h, w, k) = list(map(int, input().split()))
dp = [[0 for i in range(w + 1)] for i in range(h + 1)]
dp[0][1] = 1
mod = 10 ** 9 + 7
if w > 1:
    for i in range(1, h + 1):
        for j in range(2 ** (w - 1)):
            st = format(j, '0%ib' % (w - 1))
            flag = True
            for _ in range(w - 2):
                if st[_] == '1' and st[_ + 1] == '1':
                    flag = False
            connect = [False for kyopuro in range(w + 1)]
            if flag:
                li = []
                for ss in range(w - 1):
                    if st[ss] == '1':
                        li.append(ss + 1)
                        connect[ss + 1] = True
                        connect[ss + 2] = True
                for some in li:
                    dp[i][some + 1] += dp[i - 1][some]
                    dp[i][some + 1] %= mod
                    dp[i][some] += dp[i - 1][some + 1]
                    dp[i][some] %= mod
                for number in range(1, w + 1):
                    if connect[number] == False:
                        dp[i][number] += dp[i - 1][number]
                        dp[i][number] %= mod
    print(dp[h][k] % mod)
else:
    print(1)
