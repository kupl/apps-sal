
        
def main():
    import sys
    def input(): return sys.stdin.readline().rstrip()

    n = int(input())
    inf = 1 << 18
    dp = [inf]*(n+1)
    dp[0] = 0
    for i in range(n):
        dp[i+1] = min(dp[i+1], dp[i]+1)
        k = 1
        while i+6**k <= n:
            dp[i+6**k] = min(dp[i+6**k], dp[i]+1)
            k += 1
        k = 1
        while i+9**k <= n:
            dp[i+9**k] = min(dp[i+9**k], dp[i]+1)
            k += 1
    print(dp[n])


    




                
def __starting_point():
    main()
__starting_point()
