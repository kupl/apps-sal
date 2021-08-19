INF = -float('inf')


def Bellmanford(n, e):
    dp = [INF] * n
    dp[0] = 0
    for i in range(n):
        for (a, b, c) in e:
            if dp[a] != INF and dp[a] + c > dp[b]:
                dp[b] = dp[a] + c
                if i == n - 1 and b == n - 1:
                    return 'inf'
    return dp[n - 1]


(N, M) = map(int, input().split())
abc = []
for i in range(M):
    (a, b, c) = map(int, input().split())
    abc.append((a - 1, b - 1, c))
ans = Bellmanford(N, abc)
print(ans)
