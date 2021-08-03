import numpy as np
import sys
readline = sys.stdin.readline


N, K = list(map(int, readline().split()))
A = np.array(readline().split(), dtype=int)

nega_list = A[A < 0]
posi_list = A[A > 0]
zero_num = A[A == 0].size

nega_list = np.sort(nega_list)
posi_list = np.sort(posi_list)

nega_cnt = nega_list.size * posi_list.size
posi_cnt = ((posi_list.size * posi_list.size - 1) // 2) + ((nega_list.size * nega_list.size - 1) // 2)

zero_cnt = (zero_num * (zero_num - 1)) // 2 + zero_num * (nega_list.size + posi_list.size)

# Kがどこに属するかを判断
if K <= nega_cnt:
    # 負の数が答え
    # かけてX以下になる組み合わせをK個以上作れればOK

    def isOkNega(x):
        return np.searchsorted(nega_list, x // posi_list, side="right").sum() >= K

    ok = 0
    ng = -10**18 - 1
    while (ok - ng) > 1:
        mid = (ok + ng) // 2
        if isOkNega(mid):
            ok = mid
        else:
            ng = mid
    print(ok)

elif K <= nega_cnt + zero_cnt:
    # 0が答え
    print((0))

else:
    # 正の数が答え
    K -= (nega_cnt + zero_cnt)
    # 正のグループ内の積、負のグループ内の積、それぞれを合わせてX以下の数をK個以上作れる

    # 負の数リストは、掛け合わせた絶対値が小さいものを求める必要があるため、正のリストに変更
    nega_list = np.flipud(nega_list * (-1))

    # 自分自身との積は除外する必要があるため、自分同士の積リストを作成
    self_nega = nega_list * nega_list
    self_posi = posi_list * posi_list

    def isOkPosi(x):
        # 重複を考えずに、負の数同士の積で条件を満たすものをカウント
        nega_all = np.searchsorted(nega_list, x // nega_list, side="right")

        # 自分自身を掛け合わせたもので、条件を満たすものの個数はカウントから除外する必要がある
        nega_cnt = nega_all.sum() - self_nega[self_nega <= x].size

        # 同じペアを二回数えているため1/2する
        nega_cnt //= 2

        # 正の数リストで同じことをする
        posi_all = np.searchsorted(posi_list, x // posi_list, side="right")
        posi_cnt = posi_all.sum() - self_posi[self_posi <= x].size
        posi_cnt //= 2

        return nega_cnt + posi_cnt >= K

    ok = 10**18 + 1
    ng = 0
    while abs(ok - ng) > 1:
        mid = abs(ok + ng) // 2
        if isOkPosi(mid):
            ok = mid
        else:
            ng = mid
    print(ok)
