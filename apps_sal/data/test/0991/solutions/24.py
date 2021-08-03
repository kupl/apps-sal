import heapq as hq
N, M, S = list(map(int, input().split()))
# Edge
E = [[] for _ in range(N)]

for _ in range(M):
    # U <-> V, A coins, B mins
    u, v, a, b = list(map(int, input().split()))
    # 0-indexed
    E[u - 1].append([v - 1, a, b])
    E[v - 1].append([u - 1, a, b])

# City
C = []
for _ in range(N):
    # C coins, D mins
    C.append(list(map(int, input().split())))

# dp[p][i] 点Pにたどり着いた時、i円持っている時の最小時間
MAXYEN = 50 * N
dp = [[1e18 for i in range(MAXYEN + 5)] for _ in range(N)]
S = min(MAXYEN, S)
dp[0][S] = 0

# 状態は点とお金と時間. time, pointindex, money
Q = []
hq.heapify(Q)
hq.heappush(Q, [0, 0, S])

while len(Q) > 0:
    nowt, nowi, nowm = hq.heappop(Q)
    #print("Pop :", nowt, nowi, nowm)
    # Edgeをわたる。a yen払ってB時間かけて、Vに移動する。
    for e in E[nowi]:
        to_i, costm, costt = e
        #print("Edge:", to_i, costm, costt)
        if nowm - costm < 0:
            # unreachable
            continue
        if dp[to_i][nowm - costm] > dp[nowi][nowm] + costt:
            dp[to_i][nowm - costm] = dp[nowi][nowm] + costt
            hq.heappush(Q, [dp[nowi][nowm] + costt, to_i, nowm - costm])

    # その場でお金を1回買う。移動せず、CYenGetして、D時間かける
    getm, costt = C[nowi]
    targetm = min(MAXYEN, nowm + getm)
    #print("Buy :", getm, targetm, costt)
    if dp[nowi][targetm] > dp[nowi][nowm] + costt:
        dp[nowi][targetm] = dp[nowi][nowm] + costt
        hq.heappush(Q, [dp[nowi][targetm], nowi, targetm])

for i in range(1, N):
    print((min(dp[i])))
