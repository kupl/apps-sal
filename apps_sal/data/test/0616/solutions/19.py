from collections import defaultdict
N, M = map(int, input().split())
INF = float('inf')
dic = defaultdict(lambda: INF)
for i in range(M):
    a, b = map(int, input().split())
    c = list(map(int, input().split()))
    d = 0
    for k in c:
        d |= (1 << (k - 1))
    dic[d] = min(dic[d], a)

dp = [INF] * (1 << N)
dp[0] = 0
for k, v in dic.items():
    for b in range((1 << N) - 1):
        if dp[b] == INF:
            continue
        if b == (b | k):
            continue
        dp[b | k] = min(dp[b | k], dp[b] + v)
print(-1 if dp[-1] == INF else dp[-1])
