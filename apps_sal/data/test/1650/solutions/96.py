mod = 10 ** 9 + 7

L = input()
N = len(L)

dp = [[0] * 2 for _ in range(N + 10)]
dp[0][0] = 1

for i in range(N):
    nd = int(L[i])
    for a in range(2):
        for b in range(2):
            if a == b == 1:
                continue
            for k in range(2):
                ni = i + 1
                nk = k
                if nk == 0:
                    if nd == 1 and a == 0 and b == 0:
                        nk += 1
                    if nd == 0 and a | b > 0:
                        continue
                dp[ni][nk] += dp[i][k]
                dp[ni][nk] %= mod

ans = 0
for k in range(2):
    ans += dp[N][k]
    ans %= mod

print(ans)
