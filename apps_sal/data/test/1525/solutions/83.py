def main():
    mod = 10**9 + 7
    h, w, k = map(int, input().split())

    if w == 1:
        print(1)
        return
    if w == 2:
        print(pow(2, h-1, mod))
        return

    k -= 1

    fibo = [1, 2, 3, 5, 8, 13, 21]

    dp = [0] * w
    dp[0] = 1
    for _ in range(h):
        new_dp = [0] * w
        new_dp[0] = (dp[0] * fibo[w-2] + dp[1] * fibo[w-3]) % mod
        new_dp[1] = (dp[0] * fibo[w-3]) % mod
        new_dp[w-1] = (dp[w-1] * fibo[w-2] + dp[w-2] * fibo[w-3]) % mod
        new_dp[w-2] += (dp[w-1] * fibo[w-3]) % mod
        for i in range(1, w-1):
            new_dp[i] += ((fibo[i-1] * fibo[w-i-2]) * dp[i]) % mod
        for i in range(1, w-2):
            new_dp[i] += (fibo[i-1] * fibo[w-i-3]) * dp[i+1]
            new_dp[i] %= mod
            new_dp[i+1] += (fibo[i-1] * fibo[w-i-3]) * dp[i]
            new_dp[i+1] %= mod
        dp = new_dp

    print(dp[k] % mod)

main()
