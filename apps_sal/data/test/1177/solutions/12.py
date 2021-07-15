from sys import stdin
mod = 998244353
def main():
    N,S = list(map(int,stdin.readline().split()))
    a = list(map(int,stdin.readline().split()))
    dp = [0]*(S+1)
    ans = 0
    for A in a:
        dp[0] += 1
        for i in reversed(list(range(A,S+1))):
            dp[i] += dp[i-A]    
            dp[i] %= mod
        ans += dp[S]
        ans %= mod
    print(ans)
def __starting_point():
    main()

__starting_point()
