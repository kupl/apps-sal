def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])
    if temp != 1:
        arr.append([temp, 1])
    if arr == []:
        arr.append([n, 1])
    return arr


N = int(input())
mod = 10**9 + 7
if N == 1:
    print(1)
else:
    ans = 1
    dp = [0] * 1001
    for i in range(2, N + 1):
        p = factorization(i)
        for i, j in p:
            dp[i] += j
    for i in range(1001):
        ans *= (dp[i] + 1)
        ans %= mod
    print(ans)
