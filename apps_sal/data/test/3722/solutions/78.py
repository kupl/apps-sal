N = int(input())
caa = input()
cab = input()
cba = input()
cbb = input()
mod = 10**9 + 7
if N <= 3 or (caa == 'A' and cab == 'A') or (cab == 'B' and cbb == 'B'):
    print(1)
elif (caa == 'B' and cab == 'A' and cba == 'B') or (cab == 'B' and cba == 'A' and cbb == 'A'):
    print(pow(2, N - 3, mod))
else:
    dp = [0] * (N + 1)
    dp[2] = 1
    for i in range(3, N + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % mod
    print(dp[N])
