n = int(input())
mod = 10 ** 9 + 7
dp = [{} for _ in range(n + 1)]
moji = ['A', 'C', 'G', 'T']
for c1 in moji:
    for c2 in moji:
        for c3 in moji:
            mojis = c1 + c2 + c3
            if mojis in ['AGC', 'GAC', 'ACG']:
                continue
            if mojis in dp[3]:
                dp[3][mojis] += 1
            else:
                dp[3][mojis] = 1
for i in range(4, n + 1):
    for c in moji:
        for c1 in moji:
            for c2 in moji:
                for c3 in moji:
                    mojis = c1 + c2 + c3
                    if mojis in ['AGC', 'GAC', 'ACG']:
                        continue
                    nowmoji = c2 + c3 + c
                    if nowmoji in ['AGC', 'GAC', 'ACG']:
                        continue
                    if c1 == 'A' and c3 == 'G' and (c == 'C'):
                        continue
                    if c1 == 'A' and c2 == 'G' and (c == 'C'):
                        continue
                    if nowmoji in dp[i]:
                        dp[i][nowmoji] += dp[i - 1][mojis] % mod
                        dp[i][nowmoji] %= mod
                    else:
                        dp[i][nowmoji] = dp[i - 1][mojis] % mod
                        dp[i][nowmoji] %= mod
print(sum(dp[n].values()) % mod)
