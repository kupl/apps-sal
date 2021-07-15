def main():
    mod = 998244353
    n = int(input())
    ab = sorted([tuple(map(int, input().split())) for _ in [0]*n])
    next_idx = [-1]*n
    for i in range(n-1, -1, -1):
        dist = sum(ab[i])
        now = i
        while now < n-1:
            a1, b1 = ab[now+1]
            if a1 < dist:
                now = next_idx[now+1]
            else:
                break
        next_idx[i] = now
    dp = [0]*(n+1)
    dp[n] = 1
    for i in range(n-1, -1, -1):
        dp[i] = (dp[i+1]+dp[next_idx[i]+1]) % mod
    print(dp[0])
 
 
main()
