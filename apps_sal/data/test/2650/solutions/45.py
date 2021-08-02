import heapq as hq
from collections import defaultdict as ddict
import sys
readline = sys.stdin.readline

N, Q = list(map(int, readline().split()))

# 園児の情報[レート, 現在の園]をindexで取得できるように管理する
# 転園したら、"現在の園"を常に更新する
# 全ての園について、(-rate, 園児のID)で園児情報を持つ
# heapqで最強の園児(rate * -1)を確認できるようにする（popしない）
# 取り出した園児の所属を調べて、現在の所属と異なるようであれば破棄（転園済）
# 破棄するときに初めてpopする

# 全体については、(最強園児のレート, 園の番号)を管理するheapqを持つ
# 転園があると最強レートが変わり得るため、毎回の処理ごとに
# ・転園元の園の最新の(最強園児のレート, 園の番号)
# ・転園先の園の最新の(最強園児のレート, 園の番号)
# をheapqに格納する
# 先頭の園について、園の最強レートと照合して（正負に注意）、
# 一致しなければ情報が古いので破棄(pop)

NN = 2 * (10 ** 5)
#NN = 4
infants = [None] * (N + 1)
kinda = [[] for i in range(NN + 1)]  # (-1 * レート,園児ID)
for i in range(N):
    a, b = list(map(int, readline().split()))
    infants[i + 1] = [a, b]
    hq.heappush(kinda[b], (-a, i + 1))

# print("kinda",kinda)
# 全体の最強園児情報　（最強園児のレート, 園の番号）
all_kinda = []  # (レート, 園の番号)
# 最初に、現在の最強園児を全て格納する
for i in range(len(kinda)):
    if kinda[i]:
        hq.heappush(all_kinda, ((-1) * (kinda[i][0][0]), i))

# print("all_kinda",all_kinda)


def search_max_rate_from_kinda(x):  # ある園の最強レートを正の数で返す
    q = kinda[x]
    while q:
        rate, infant_id = q[0]  # レートは負の数
        # 取り出した園児が、現在もxに所属しているかを調べる
        if infants[infant_id][1] != x:
            # 転園済
            hq.heappop(q)
        else:
            # 現在も所属している
            return -rate  # 正負を反転して返す
    return -1  # 全員が転園済みだった場合


for i in range(Q):
    target, new_kinda_id = list(map(int, readline().split()))  # 園児, 転園先
    # 現在の園とレートを調べる
    rate, old_kinda_id = infants[target]
    # 現在の園を最新に保つ
    infants[target][1] = new_kinda_id
    # 転園先に園児を追加する
    hq.heappush(kinda[new_kinda_id], (-rate, target))

    # 転園元の園の最強レートを取り出し、全体のキューに追加
    old_kinda_rate = search_max_rate_from_kinda(old_kinda_id)
    if old_kinda_rate != -1:
        hq.heappush(all_kinda, (old_kinda_rate, old_kinda_id))

    # 転園先の園の最強レートを取り出し、全体のキューに追加
    new_kinda_rate = search_max_rate_from_kinda(new_kinda_id)
    if new_kinda_rate != -1:
        hq.heappush(all_kinda, (new_kinda_rate, new_kinda_id))

    # print("i",i,"kinda",kinda)
    # print("i",i,"all_kinda",all_kinda)
    # 全体のキューの先頭にいる(最弱レート, 園の番号)について、
    # その園の最強園児と一致していれば出力する
    while all_kinda:
        weakest_rate, kinda_id = all_kinda[0]
        current_max_rate = search_max_rate_from_kinda(kinda_id)
        if weakest_rate != current_max_rate:
            # 情報が古い
            hq.heappop(all_kinda)
        else:
            print(weakest_rate)
            break
