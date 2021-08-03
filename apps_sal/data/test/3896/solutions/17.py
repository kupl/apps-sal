MOD = 1000000007
str = input()
l = len(str)


def b2d(str):
    ans = 0
    cnt = 0
    str = str[::-1]
    for k in str:
        if k == '1':
            ans += pow(2, cnt)
            ans %= MOD
        cnt += 1
    return ans


print((b2d(str) * pow(2, l - 1)) % MOD)
