s = int(input())
d = [[0] * (s + 1) for i in range((s + 2) // 3 + 1)]
d[0][0] = 1
ans = 0
MOD = 1000000007
for i in range((s + 2) // 3):
    sum = 0
    for js in range(s + 1):
        if 3 <= js:
            sum += d[i][js - 3]
        sum %= MOD
        d[i + 1][js] += sum
        d[i + 1][js] %= MOD
    ans += d[i + 1][s]
print(ans % MOD)
