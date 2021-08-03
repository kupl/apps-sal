from heapq import heappush, heappop
import sys
# sys.setrecursionlimit(10**7)  # ネスト回数制限（いる？）

# 入力値を扱いやすい形で格納していく

# input=sys.stdin.buffer.readline  # input の高速化（今回は外す）

N, M, S = map(int, input().split())  # 頂点数／辺数／初期所持金(state)
S = min(S, 2500)  # 高々 2500 あれば良い（全都市を回るのに払いきれる回数）

INF = 10**18
dp = [[INF] * 2501 for _ in range(N)]
way = [[]for _ in range(N)]

for _ in range(M):
    u, v, a, b = map(int, input().split())
    way[u - 1].append((v - 1, a, b))
    way[v - 1].append((u - 1, a, b))

# 両替比率と時間
# CD = [list(map(int,input().split())) for _ in range(N)]  # list化する意味は？
CD = [tuple(map(int, input().split())) for _ in range(N)]


# q は 時間／都市名／所持金　の順番 <- 時間をキーに heapq を使うため

q = [(0, 0, S)]  # スタート状態

while q:
    t, u, s = heappop(q)  # 最も到着時間の短い都市 u を選択
    for nxt, a, b in way[u]:  # u からたどり着ける都市 nxt に対して
        if s >= a:  # 交通費がある場合

            if dp[nxt][s - a] > t + b:  # 到着時間を検討
                dp[nxt][s - a] = t + b  # 早いので書き換え
                heappush(q, (t + b, nxt, s - a))  # キューに次の都市候補として登録しておく
                # 同じ都市 & 同じ金額 が複数個登録されないか？ 計算回数は
                # 更新された = 周囲の都市（点）にたどり着く値を更新する必要があるかもしれないから
                # 検討対象になる

        # この時点では、u にいて、所持金 s でたどり着けないとしてはまだ更新されていない

    c, d = CD[u]
    nc = min(2500, c + s)  # 所持金を増やす
    nt = t + d  # 時間も掛かる

    if nt < dp[u][nc]:  # 交換後の金額と時間を見て、更新する（無限大だけが更新になる？）
        dp[u][nc] = nt
        heappush(q, (nt, u, nc))  # 同じ都市（点）だが、違う状態が登録されている

for i in range(1, N):
    print(min(dp[i]))
