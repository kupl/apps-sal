from collections import deque
import math

N, D, A = list(map(int, input().split()))
XH = [list(map(int, input().split())) for _ in range(N)]
XH.sort(key=lambda x: x[0])

# 爆発範囲がとても広く、全ての爆発が右端まで及ぶとひとまず考える
# 各xを見る際に、影響の及ばない爆発分のダメージは引く

# 合計の爆発回数
ans = 0
# 爆発ダメージの合計
total_damage = 0
# 各爆発の情報
dq = deque()

# 左端から順にモンスターを見る
for x, h in XH:
    # 爆発が及ばない場合
    while dq and dq[0][1] < x:
        dmg, rng = dq.popleft()
        total_damage -= dmg

    # 爆発させる必要がある場合
    if total_damage < h:
        # 残っているHPに更新
        h -= total_damage
        # 必要な爆発回数
        cnt = math.ceil(h / A)
        ans += cnt
        # 爆発回数 * 単発のダメージ
        dmg = cnt * A
        total_damage += dmg
        # [爆発で与えるダメージ、及ぶ範囲の右端]
        dq.append((dmg, x + D * 2))

print(ans)

