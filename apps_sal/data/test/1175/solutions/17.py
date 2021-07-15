L, R = map(int, input().split())
MOD = 10**9 + 7

*BL, = map(int, bin(L)[2:])
*BR, = map(int, bin(R)[2:])

a = len(BL)
b = len(BR)
BL = [0]*(len(BR) - len(BL)) + BL

BL.reverse()
BR.reverse()

memo = [[[-1]*2 for i in range(2)] for j in range(70)]
def dfs(i, p, q):
    if memo[i][p][q] != -1:
        return memo[i][p][q]
    if i == -1:
        memo[i][p][q] = 1
        return 1
    r = 0
    if p == q == 0:
        if BL[i] == 1 and BR[i] == 0:
            memo[i][0][0] = 0
            return 0
        if BL[i] == 1 or BR[i] == 0:
            r = dfs(i-1, 0, 0)
        else:
            r = (dfs(i-1, 0, 1) + dfs(i-1, 1, 0) + dfs(i-1, 0, 0)) % MOD
    elif p == 0:
        if BL[i] == 1:
            r = dfs(i-1, 0, 1)
        else:
            r = (2*dfs(i-1, 0, 1) + dfs(i-1, 1, 1)) % MOD
    elif q == 0:
        if BR[i] == 0:
            r = dfs(i-1, 1, 0)
        else:
            r = (2*dfs(i-1, 1, 0) + dfs(i-1, 1, 1)) % MOD
    else:
        r = 3 * dfs(i-1, 1, 1)
    memo[i][p][q] = r
    return r
ans = 0
for l in range(a-1, b):
    ans += dfs(l-1, +(not a-1 == l), +(not b-1 == l))
print(ans % MOD)
