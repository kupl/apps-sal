import sys
stdin = sys.stdin

sys.setrecursionlimit(10**5)


def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x) - 1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())


n, l, r = li()
MOD = 10**9 + 7

st = l % 3
lg = (r - l + 1) // 3
mods = [lg] * 3
for i in range((r - l + 1) - 3 * lg):
    mods[st] += 1
    st += 1
    st %= 3

dp = [[0] * 3 for _ in range(n + 1)]
dp[0][0] = 1

for i in range(n):
    dp[i + 1][0] = dp[i][0] * mods[0] % MOD + dp[i][1] * mods[2] % MOD + dp[i][2] * mods[1] % MOD
    dp[i + 1][1] = dp[i][0] * mods[1] % MOD + dp[i][1] * mods[0] % MOD + dp[i][2] * mods[2] % MOD
    dp[i + 1][2] = dp[i][0] * mods[2] % MOD + dp[i][1] * mods[1] % MOD + dp[i][2] * mods[0] % MOD

    dp[i + 1][0] %= MOD
    dp[i + 1][1] %= MOD
    dp[i + 1][2] %= MOD

print(dp[-1][0])
