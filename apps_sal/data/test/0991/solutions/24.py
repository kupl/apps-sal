import heapq as hq
N, M, S = list(map(int, input().split()))
E = [[] for _ in range(N)]

for _ in range(M):
    u, v, a, b = list(map(int, input().split()))
    E[u - 1].append([v - 1, a, b])
    E[v - 1].append([u - 1, a, b])

C = []
for _ in range(N):
    C.append(list(map(int, input().split())))

MAXYEN = 50 * N
dp = [[1e18 for i in range(MAXYEN + 5)] for _ in range(N)]
S = min(MAXYEN, S)
dp[0][S] = 0

Q = []
hq.heapify(Q)
hq.heappush(Q, [0, 0, S])

while len(Q) > 0:
    nowt, nowi, nowm = hq.heappop(Q)
    for e in E[nowi]:
        to_i, costm, costt = e
        if nowm - costm < 0:
            continue
        if dp[to_i][nowm - costm] > dp[nowi][nowm] + costt:
            dp[to_i][nowm - costm] = dp[nowi][nowm] + costt
            hq.heappush(Q, [dp[nowi][nowm] + costt, to_i, nowm - costm])

    getm, costt = C[nowi]
    targetm = min(MAXYEN, nowm + getm)
    if dp[nowi][targetm] > dp[nowi][nowm] + costt:
        dp[nowi][targetm] = dp[nowi][nowm] + costt
        hq.heappush(Q, [dp[nowi][targetm], nowi, targetm])

for i in range(1, N):
    print((min(dp[i])))
