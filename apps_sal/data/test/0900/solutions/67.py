
# dp[i][k] := 先頭i桁を13で割った余りがkとなるものの個数 or
# dp[i][k] := 先頭i桁（残りはすべて0）を13で割った余りがkとなるものの個数
# どちらが良いか?
# 後者で。
# 先頭からでも下位からでもアルゴリズムは同じはず。下位からのほうが添え字が見やすい。
# →尺取っぽくやるのは下位の桁を追加したときだ。上位から決めないとダメじゃね?
# →前者じゃないとダメか。

# 配るDP
# 桁dがあれば：dp[i+1][k+ (d * 10 ** a)% 13] = dp[i][k]
# 桁が?ならば：10通りあるから10回配る? dp[i+1][k+ (d * 10 ** a)% 13] = dp[i][k]
# 10^5 * 10 * 13は無理じゃない?
# 全体-残り3つとして、+-しながら管理　（これができるのは1の桁の場合だけ）

s = input()
l = len(s)
dp = [[0 for _ in range(13)] for _ in range(l+1)]
dp[0][0] = 1
temp = [0] * 13
summ = 1
mod = 10 ** 9 + 7

for i in range(0, l):
    if s[i] != '?':
        for k in range(13):
            dp[i+1][(k*10+int(s[i])) % 13] = dp[i][k]
    else:
        # ?の場合
        for k in range(13):
            temp[(k*10) % 13] = dp[i][k]
        
        excluded = temp[1] + temp[2] + temp[3]
        for k in range(13):
            dp[i+1][k] = (summ - excluded) % mod
            excluded -= temp[(k+1)%13]
            excluded += temp[(k+4)%13]

        summ *= 10
        summ %= mod

print((dp[l][5]))
# print(dp)            



