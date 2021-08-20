(N, M) = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)
d = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]
S = set()
for a in A:
    S.add(d[a])
INF = 10 ** 8
dp = [-INF for _ in range(N + 1)]
dp[0] = 0
for i in range(N + 1):
    for s in S:
        if i - s >= 0:
            dp[i] = max(dp[i], dp[i - s] + 1)
ans = 0
digit = dp[N]
for i in range(digit - 1, -1, -1):
    if i != 0:
        for a in A:
            if dp[N - d[a]] == i:
                ans = ans * 10 + a
                N -= d[a]
                break
    else:
        for a in A:
            if N == d[a]:
                ans = ans * 10 + a
                break
print(ans)
