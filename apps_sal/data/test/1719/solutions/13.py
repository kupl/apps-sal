from collections import defaultdict

MOD = 10 ** 9 + 7

N = int(input())


"""dp = dict()
for c1 in "ACGT":
    for c2 in "ACGT":
        for c3 in "ACGT":
            for c4 in "ACGT":
                s = c1 + c2 + c3 + c4
                if s[0:3] in ("AGC", "ACG", "GAC"):
                    continue
                if s[1:4] in ("AGC", "ACG", "GAC"):
                    continue
                if s in ("AGGC", "AGTC", "ATGC"):
                    continue

                dp[s] = 1"""

dp = {"TTT": 1}
for _ in range(N):
    new_dp = defaultdict(int)
    for s, count in dp.items():
        new_dp[s[1:] + 'A'] += count
        new_dp[s[1:] + 'T'] += count
        if s[1:] != "AC":
            new_dp[s[1:] + 'G'] += count
        if s not in ("AGG", "AGT", "ATG") and s[1:] not in ("AG", "GA"):
            new_dp[s[1:] + 'C'] += count

    dp = dict()
    for k, v in new_dp.items():
        dp[k] = v % MOD

print(sum(dp.values()) % MOD)
