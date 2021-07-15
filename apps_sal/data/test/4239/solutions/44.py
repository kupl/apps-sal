from functools import lru_cache

def main():
    n=int(input())
    dp=[float("inf")]*(n+1)
    dp[0]=0
    for i in range(n):
        dp[i+1] = min(dp[i+1], dp[i]+1)
        j,k = 6,9
        while i+j <= n:
            dp[i+j] = min(dp[i+j], dp[i]+1)
            j *= 6
        while i+k <= n:
            dp[i+k] = min(dp[i+k], dp[i]+1)
            k *= 9
    print(dp[-1])

def __starting_point():
    main()
__starting_point()
