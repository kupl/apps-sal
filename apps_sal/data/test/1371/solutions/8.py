def solve():
    a = 10**9 + 7
    s = int(input())
    dp = [0] * (s+1)
    dp[0] = 1
    for i in range(3, s+1):
        dp[i] = (dp[i-1] + dp[i-3]) % a
    
    print(dp[s])
 
solve()
