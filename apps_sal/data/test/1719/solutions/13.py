from collections import defaultdict
MOD = 10 ** 9 + 7
N = int(input())
'dp = dict()\nfor c1 in "ACGT":\n    for c2 in "ACGT":\n        for c3 in "ACGT":\n            for c4 in "ACGT":\n                s = c1 + c2 + c3 + c4\n                if s[0:3] in ("AGC", "ACG", "GAC"):\n                    continue\n                if s[1:4] in ("AGC", "ACG", "GAC"):\n                    continue\n                if s in ("AGGC", "AGTC", "ATGC"):\n                    continue\n\n                dp[s] = 1'
dp = {'TTT': 1}
for _ in range(N):
    new_dp = defaultdict(int)
    for (s, count) in dp.items():
        new_dp[s[1:] + 'A'] += count
        new_dp[s[1:] + 'T'] += count
        if s[1:] != 'AC':
            new_dp[s[1:] + 'G'] += count
        if s not in ('AGG', 'AGT', 'ATG') and s[1:] not in ('AG', 'GA'):
            new_dp[s[1:] + 'C'] += count
    dp = dict()
    for (k, v) in new_dp.items():
        dp[k] = v % MOD
print(sum(dp.values()) % MOD)
