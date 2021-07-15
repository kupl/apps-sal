n = int(input())
m = 998244353
dp = [1] + [0] * n;
for i in map(int, input().split()) :
    v = dp[:]
    if(0 < i < n) :
        v[i] = (v[i] + v[0]) % m
    for j in range(n) :
        v[j] = (v[j] + dp[j + 1]) % m
    dp = v
print((dp[0] - 1) % m)

