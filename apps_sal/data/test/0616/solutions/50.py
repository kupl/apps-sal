INF = 10**9
n, m = list(map(int, input().split()))
keys = []
for _ in range(m):
    a, _ = list(map(int, input().split()))
    c = 0
    for i in input().split():
        c += 2**(int(i)-1)
    keys.append((a, c))

dp = [INF]*(2**n)
dp[0] = 0
for a, c in keys:
    tmp = [INF]*(2**n)
    for j, d in enumerate(dp):
        if d == INF:
            continue
        if d < tmp[j]:
            tmp[j] = d
        if d+a < tmp[j|c]:
            tmp[j|c] = d+a
    dp = tmp

print((dp[-1] if dp[-1]<INF else -1))

