
mod = int(1e9 + 7)

n = int(input())
a = [int(_) for _ in input().split()]

freq = {i: 0 for i in range(100001)}
power = {0: 1}
for i in range(1, 100001):
    power[i] = (2 * power[i - 1]) % mod

for v in a:
    freq[v] += 1

dp = {i: 0 for i in range(100001)}
for gcd in range(100000, 0, -1):
    mult = 2
    total = freq[gcd]
    complement = 0
    # xy = k, so integral is ln(x)
    while mult * gcd <= 100000:
        total += freq[mult * gcd]
        complement += dp[mult * gcd]
        mult += 1
    dp[gcd] = (power[total] - 1 - complement + mod) % mod

print(dp[1])
