# 解説放送
# 解説PDFは「効果範囲がどのモンスターか」を事前に求めているが、
# 解説放送ではキューを使うことで「効果範囲がどのモンスターか」を求めず、座標のみでうまく処理している
# 解説放送だとBITを使った解法もある

# 貪欲の方針は見えやすい。そこから2つの難題がある
# (1) 効果範囲。単純に調べるとO(N^2)
# → 二分探索、尺取り法（事前に全計算でも逐次処理と同時に計算でも良い）
# (2) HPの減算。多数の要素に対してAを引く必要があり、最悪O(N^2)
# →一定範囲に-Aするのは時間がかかるけど、最初に-Aして最後に+Aすれば2要素を変えるだけで済むね（imos法）

import collections
n, d, a = list(map(int, input().split()))
enemies = [list(map(int, input().split())) for _ in range(n)]

enemies.sort(key=lambda a: a[0])  # 座標を基準にソート

d *= 2
total_damage = 0

q = collections.deque()

ans = 0
for i in range(n):
    x = enemies[i][0]
    hp = enemies[i][1]

    while (len(q) and q[0][0] < x):
        total_damage -= q[0][1]
        q.popleft()

    hp -= total_damage
    if hp > 0:
        times = (hp + a - 1) // a
        total_damage += a * times
        ans += times

        q.append((x + d, a * times))

print(ans)
