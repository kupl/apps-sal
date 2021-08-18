N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
A.sort(reverse=True)

match = [10**18, 2, 5, 5, 4, 5, 6, 3, 7, 6]

dp = [-10**18] * (N + 1)
dp[0] = 1

for i in range(N):
    for a in A:
        m = match[a]
        if i + m <= N and dp[i + m] < dp[i] + 1:
            dp[i + m] = dp[i] + 1

ans = []
while N > 0:
    for a in A:
        m = match[a]
        if N - m >= 0 and dp[N - m] + 1 == dp[N]:
            ans.append(a)
            N -= m
            break

ans.sort(reverse=True)

print((''.join(map(str, ans))))
