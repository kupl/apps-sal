# 写経AC

from heapq import heappop,heappush

INF = 10 ** 18

N, K = map(int, input().split())
# S[i]: 種類iの美味しさの集合
S = [[] for _ in range(N)]
for _ in range(N):
    t,d = map(int, input().split())
    S[t-1].append(d)

# 各種類について、美味しい順に並べる
for i in range(N):
    S[i].sort(reverse = True)
    if not S[i]: S[i].append(-INF) # 番兵

# 「美味しさの最大値」の降順でソート
S.sort(reverse = True)

uma = 0 # おいしさ基礎ポイント
que = [] # 選ばれていない寿司の美味しさリスト
for i in range(K):
    # ある種類の一番美味しい寿司を選ぶ
    uma += S[i][0]
    for j in range(1, len(S[i])):
        heappush(que, (-1) * S[i][j])

# 残りの寿司もリストに追加
for i in range(K, N):
    for j in range(len(S[i])):
        heappush(que, (-1) * S[i][j])

ans = uma + K * K
# 種類を減らしていく
for x in range(K - 1, 0, -1):
    v = S[x][0] # 選ばれている最小の「おいしさ」
    w = (-1) * que[0] # 選ばれていない最大の「おいしさ」
    if v < w:
        heappop(que)
        heappush(que, (-1) * v)
        uma -= v; uma += w
    ans = max(ans, uma + x * x)

print(ans)
