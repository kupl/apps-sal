n = int(input())
MOD = 10**9 + 7
d = {"A": 0, "C": 1, "G": 2, "T": 3}
dic = {}
dic_r = {}
for i0 in "ACGT":
    for i1 in "ACGT":
        for i2 in "ACGT":
            v = 4**2 * d[i2] + 4 * d[i1] + d[i0]
            k = i2 + i1 + i0
            dic[k] = v
            dic_r[v] = k

dp = [[0] * 64 for i in range(n)]
for i in range(64):
    dp[0][i] = 1
dp[0][dic["AGC"]] = 0
dp[0][dic["ACG"]] = 0
dp[0][dic["GAC"]] = 0
for i in range(n - 3):
    for j in range(64):
        v = dic_r[j]
        for s in "ACGT":
            # AG*C
            if v[0] == "A" and v[1] == "G":
                if s != "C":
                    new = v[1] + v[2] + s
                    dp[i + 1][dic[new]] += dp[i][dic[v]]
            # A*GC
            elif v[0] == "A" and v[2] == "G":
                if s != "C":
                    new = v[1] + v[2] + s
                    dp[i + 1][dic[new]] += dp[i][dic[v]]
            # *GAC
            elif v[1] == "G" and v[2] == "A":
                if s != "C":
                    new = v[1] + v[2] + s
                    dp[i + 1][dic[new]] += dp[i][dic[v]]
            # *ACG
            elif v[1] == "A" and v[2] == "C":
                if s != "G":
                    new = v[1] + v[2] + s
                    dp[i + 1][dic[new]] += dp[i][dic[v]]
            # *AGC
            elif v[1] == "A" and v[2] == "G":
                if s != "C":
                    new = v[1] + v[2] + s
                    dp[i + 1][dic[new]] += dp[i][dic[v]]
            else:
                new = v[1] + v[2] + s
                dp[i + 1][dic[new]] += dp[i][dic[v]]
    continue
print((sum(dp[n - 3]) % MOD))
