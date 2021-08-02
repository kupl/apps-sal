from collections import Counter

S = input()
n = len(S)
dp = [[0] * n for _ in range(20)]

for i, s in enumerate(S):
    dp[0][i] = i - 1 if s == 'L' else i + 1

for k in range(19):
    for i in range(n):
        dp[k + 1][i] = dp[k][dp[k][i]]

C = Counter(dp[-1])

print(*[C[i] for i in range(n)])
