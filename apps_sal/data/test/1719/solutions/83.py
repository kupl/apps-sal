N = int(input())
mod = int(1000000000.0) + 7
line = 'TAGC'
ng = {'AGC', 'ACG', 'GAC', 'ATGC', 'AGGC', 'ACGC', 'AGTC', 'AGCC'}
D = {line[i // 16 % 4] + line[i // 4 % 4] + line[i % 4]: i for i in range(64)}
invD = {i: line[i // 16 % 4] + line[i // 4 % 4] + line[i % 4] for i in range(64)}
dp = [[0 for _ in range(N + 1)] for __ in range(64)]
dp[0][0] = 1
for i in range(4):
    dp[i][1] = 1
for i in range(16):
    dp[i][2] = 1
for i in range(3, N + 1):
    for j in range(64):
        for k in range(4):
            last = invD[j]
            if last not in ng:
                if last[1:] + line[k] not in ng and last + line[k] not in ng:
                    dp[D[last[1:] + line[k]]][i] += dp[D[last]][i - 1]
                    dp[D[last[1:] + line[k]]][i] %= mod
S = 0
for i in range(64):
    S += dp[i][N]
    S %= mod
print(S)
