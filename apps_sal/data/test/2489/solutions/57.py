N = int(input())
A = list(map(int, input().split()))
A.sort()
Amax = A[-1]
dp = [True] * (Amax + 1)
ans = 0
for i in range(N - 1):
    p = A[i]
    if dp[p]:
        for j in range(1, Amax // p + 1):
            dp[p * j] = False
        if p != A[i + 1]:
            ans += 1
if dp[Amax]:
    ans += 1
print(ans)
