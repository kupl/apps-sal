n = int(input())
c_aa = input()
c_ab = input()
c_ba = input()
c_bb = input()
mod = 10**9 + 7
if(n == 2):
    print(1)
    return

num = 0
for ci, i in zip([c_aa, c_ab, c_ba, c_bb], [0, 1, 2, 3]):
    if(ci == 'B'):
        num += 2**i

if(num in [1, 6, 7, 9]):
    dp = [0] * (n + 1)
    dp[2] = 1
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % mod
    print(dp[-1])
    return

elif(num in [2, 3, 5, 13]):
    ans = pow(2, n - 3, mod)
    print(ans)
    return

print(1)
