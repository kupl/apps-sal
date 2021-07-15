import copy

s = list(input())

s.reverse()
n = len(s)
MOD = 2019
m = [0] * n
msum = [0] * (n+1)
cnt = [0] * (MOD)
cnt[0] = 1
t = 1
for i in range(n):
    m[i] = int(s[i]) * t % MOD
    msum[i+1] = (msum[i] + m[i]) % MOD
    cnt[msum[i+1]] += 1
    t = t * 10 % MOD

ans = 0
for i in range(MOD):
    ans += cnt[i] * (cnt[i] - 1) // 2
print(ans)
