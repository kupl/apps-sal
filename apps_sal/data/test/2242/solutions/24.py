s = list(input())
MOD = 2019
temp = 0
d = 1
m = [0] * MOD
m[0] = 1
for x in reversed(s):
    temp += int(x) * d
    temp %= MOD
    m[temp] += 1
    d = d * 10 % MOD
ans = 0
for x in m:
    ans += x * (x - 1) // 2
print(ans)
