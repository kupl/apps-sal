from heapq import heappop, heappush
# プライオリティキュー
# 要素の挿入、最小値（最大値）の取り出しが速い
# 園児の転園による削除がボトルネック
# 削除しなければ良いと考える（勿論チェックは必要）

N, Q = list(map(int, input().split()))

# 幼稚園の数
M = 2 * (10 ** 5)
# 幼児iの所属先の幼稚園
belong = [None] * N
# 幼児iのレート
rate = [None] * N
# 幼稚園キュー。(マイナスレート, 幼児番号)
# KinDerGarTen
kdgt = [[] for _ in range(M)]

for c in range(N):
    A, B = list(map(int, input().split()))
    # 幼稚園番号を0-indexにする
    B -= 1
    # 所属
    belong[c] = B
    # レート
    rate[c] = A
    # 幼稚園の箱に対して、(マイナスレート、幼児番号)
    heappush(kdgt[B], (-A, c))

# 最強園児キュー。(プラスレート, 幼児番号, 園番号)
q = []

# 各幼稚園について
for i in range(M):
    # 一人も所属していなければパス
    if kdgt[i]:
        # マイナスがかかっているので最大値が取り出せる
        A, c = kdgt[i][0]
        # (プラスレート、幼児番号、園番号)
        heappush(q, (-A, c, i))

for _ in range(Q):
    C, D = list(map(int, input().split()))
    # 幼児番号、園番号を0-indexに
    C -= 1
    D -= 1
    # 移動元の幼稚園
    pd = belong[C]
    # 幼児のbelongを更新
    belong[C] = D

    # 移動元の幼稚園キューを更新
    while kdgt[pd]:
        # その園での最強園児（仮）
        A, c = kdgt[pd][0]
        # 既に存在しないとき、取り除く
        # 存在するとき, 最強園児キューへ追加
        if belong[c] != pd:
            heappop(kdgt[pd])
        else:
            heappush(q, (-A, c, pd))
            break

    # 移動先の幼稚園キューを更新
    # 対象の幼児を追加
    heappush(kdgt[D], (-rate[C], C))
    while kdgt[D]:
        # その園での最強園児（仮）
        A, c = kdgt[D][0]
        # 既に存在しないとき取り除く
        # 存在するとき, 最強園児キューへ追加
        if belong[c] != D:
            heappop(kdgt[D])
        else:
            heappush(q, (-A, c, D))
            break

    while q:
        # 最強の中の最弱（仮）
        # (プラスレート、園児番号、園番号)
        A, c, d = q[0]
        # キューの先頭の園児が既に去っている or 所属する幼稚園キューの先頭では無い時取り除く
        # （後者について）最強の中の最弱を探したいのに、既に最強ではない園児が紛れ込む場合がある？

        # 2つの条件を確認する部分があまり理解できていない、後日改めて考える
        if belong[c] != d or kdgt[d][0][1] != c:
            heappop(q)
        else:
            print(A)
            break

