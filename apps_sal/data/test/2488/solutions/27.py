from math import ceil
from collections import deque


def main():
    N, D, A = list(map(int, input().split()))
    # 座標X[i]のモンスターはceil(H[i]/A)回攻撃すれば倒せる
    # N=5, D=2
    # 0 1 2 3 4 5 6 7 8 9 10
    # 0 5 0 2 0 0 3 3 0 0 4 (倒すのに必要な回数; 全部0にすれば終了)
    # 0 0 0 0 0 0 3 3 0 0 4 (座標3で5回爆破したあと)
    # 0 0 0 0 0 0 0 0 0 0 1 (座標8で3回爆破したあと)
    # 0 0 0 0 0 0 0 0 0 0 0 (座標10で1回爆破したあと)
    # ->よって5+3+1=9回が最小回数..?

    Monsters = sorted([list(map(int, input().split())) for i in range(N)])
    Monsters = [[x - 1, ceil(h / A)] for x, h in Monsters]

    acc_damage = 0
    que = deque([])

    ans = 0
    for x, h in Monsters:
        # 期限切れの蓄積ダメージを削除
        while que and x > que[0][0]:
            limit, damage = que.popleft()
            acc_damage -= damage

        need = max(0, h - acc_damage)
        ans += need
        acc_damage += need

        if need:
            que.append([x + 2 * D, need])

    print(ans)


main()
