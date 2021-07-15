s = str(input())
MOD = 2019
m = 0
digit = 1
mods = [1] + [0] * 2018
for a in s[::-1]:
    m = (m + digit * int(a)) % MOD
    mods[m] += 1
    digit = digit * 10 % MOD
ans = 0
for x in mods:
    ans += x * (x - 1) // 2
print(ans)
