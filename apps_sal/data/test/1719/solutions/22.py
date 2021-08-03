ACGT = ['A', 'C', 'G', 'T', '']
MOD = 10 ** 9 + 7

N = int(input())
dp = [[[[0] * 5
        for _ in range(5)]
       for _ in range(5)]
      for _ in range(N + 1)]

dp[0][4][4][4] = 1
for i in range(N):
    for p in range(5):
        for q in range(5):
            for r in range(5):
                for s in range(4):
                    if ACGT[q] + ACGT[r] + ACGT[s] not in {'AGC', 'GAC', 'ACG'} \
                            and ACGT[p] + ACGT[r] + ACGT[s] != 'AGC' \
                            and ACGT[p] + ACGT[q] + ACGT[s] != 'AGC':
                        dp[i + 1][q][r][s] += dp[i][p][q][r]
                        dp[i + 1][q][r][s] %= MOD

print((sum(sum(sum(y) for y in x) for x in dp[N]) % MOD))
