MOD = 10**9 + 7

def main():
    s = [int(in_i) if in_i != '?' else -1 for in_i in list(open(0).read())[:-1]]
    n = len(s)

    cnt = [0] * 13
    if s[0] == -1:
        for j in range(10):
           cnt[j] = 1
    else:
        cnt[s[0]] = 1

    for cur_s in s[1:]:
        dp = [0] * 26
        for i in range(13):
            dp[i*10%13] = cnt[i] % MOD
        dp[13:] = dp[:13]

        if cur_s == -1:
            for i in range(13):
                cnt[i] = sum(dp[i+4:i+14])
        else:
            for i in range(13):
                cnt[i] = dp[i+13-cur_s]

    ans = cnt[5] % MOD
    print(ans)
    return()

def __starting_point():
    main()

__starting_point()
