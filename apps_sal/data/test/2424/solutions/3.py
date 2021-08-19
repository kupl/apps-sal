import sys
input = sys.stdin.readline
MOD = 998244353
n = int(input())
info = [list(map(int, input().split())) for i in range(n)]
ans = 0
memo = {}
for i in range(n):
    for j in info[i][1:]:
        if j - 1 not in memo:
            memo[j - 1] = 1
        else:
            memo[j - 1] += 1
memo_p = {}
student_p = 1 * pow(n, MOD - 2, MOD)
pow_memo = {}
for i in range(n):
    k = info[i][0]
    if k not in pow_memo:
        pow_memo[k] = pow(k, MOD - 2, MOD)
    for j in info[i][1:]:
        if j - 1 not in memo_p:
            memo_p[j - 1] = pow_memo[k]
        else:
            memo_p[j - 1] += pow_memo[k]
        memo_p[j - 1] %= MOD
for i in memo:
    ans += memo[i] * memo_p[i]
    ans %= MOD
print(ans * student_p * student_p % MOD)
