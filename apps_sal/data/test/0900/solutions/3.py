import sys
#input = sys.stdin.buffer.readline

def main():
    s = str(input())
    l = len(s)
    ans = [0 for _ in range(13)]
    MOD = 10**9+7
    ans[0] = 1
    
    for st in s:
        dp = [0 for _ in range(13)]
        for i in range(13):
            dp[(10*i)%13] = ans[i]%MOD
        dp += dp
        if st != "?":
            for i in range(13):
                num = int(st)
                ans[i] = dp[i+13-num]
        else:
            for i in range(13):
                ans[i] = sum(dp[i+4:i+14])
    
    print(ans[5]%MOD)

def __starting_point():
    main()
__starting_point()
