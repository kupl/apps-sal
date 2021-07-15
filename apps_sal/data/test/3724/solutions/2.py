n = int(input())
s = input()
s = list(map('_ABC'.index, s))

MOD = 10 ** 9 + 7

dp = [0, 0, 0, 0]
dp[s[0]] = 1

xor = s[0]
p = 1
potential = 0
while p < n and s[p] == s[0]:
    xor ^= s[p]
    p += 1
    potential += 1

for i, c in enumerate(s[p:], start=p):

    d, e = c % 3 + 1, (c + 1) % 3 + 1

    dp[c] = sum(dp) % MOD
    dp[d], dp[e] = dp[e], dp[d]

    if potential > 0:
        if s[i - 1] == d:
            dp[c] += (potential + 1) // 2
            dp[e] += potential // 2
        else:
            dp[c] += (potential + 1) // 2
            dp[d] += potential // 2
        potential = 0
    elif xor == 0:
        dp[c] += 1
    xor ^= c

print((sum(dp) % MOD))

