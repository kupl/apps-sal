n, m = list(map(int, input().split()))
A = sorted(list(map(int, input().split())), reverse=True)
L = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]

inf = float('inf')
# dp[i]=i本で最大何桁作れるか
dp = [-inf] * (n + 1)
dp[0] = 0
for i in range(1, n + 1):
    for j in range(m):
        num = L[A[j]]
        if i >= num:
            dp[i] = max(dp[i], dp[i - num] + 1)

sort_A = sorted(A, reverse=True)
ans = ''
while True:
    if n == 0:
        break
    for i in range(m):
        temp = sort_A[i]
        num = L[temp]
        if n >= num and dp[n - num] >= 0:
            if dp[n - num] == dp[n] - 1:
                ans += str(temp)
                n -= num
                break


print((int(ans)))
