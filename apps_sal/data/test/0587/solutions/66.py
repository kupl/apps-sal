# 種類が同じ寿司であれば、最も美味しさが高い寿司を選ぶべき。
# 従い、
# (1)各種類の最も美味しさが高い寿司グループ
# (2)それ以外の寿司グループ
# をいずれも降順に並べて、(1)から幾つ取るか(最低でも1つは取る)を全探索する
from collections import defaultdict
import sys
readline = sys.stdin.readline

N, K = map(int, readline().split())

sushi = defaultdict(list)  # 種類・おいしさ　のdictionary

for i in range(N):
    t, d = map(int, readline().split())
    sushi[t].append(d)

best_sushi = []
other_sushi = []

for value in sushi.values():
    value = sorted(value, reverse=True)
    best_sushi.append(value[0])
    other_sushi += value[1:]

best_sushi = sorted(best_sushi, reverse=True)
other_sushi = sorted(other_sushi, reverse=True)

best_num = 1  # best_sushiから選ぶ個数
other_num = K - 1  # other_sushiから選ぶ個数

if len(other_sushi) < other_num:  # 選べない場合
    other_num = len(other_sushi)
    best_num = K - other_num

# それぞれの寿司から選ぶ個数の開始値が決定
# other_sushiの後ろの要素は切り離して良い

other_sushi = other_sushi[:other_num]

sushi_point = sum(best_sushi[:best_num]) + sum(other_sushi)
kind_point = best_num ** 2

ans = sushi_point + kind_point

# best寿司のインデックスを進めていく
for i in range(best_num, len(best_sushi)):
    sushi_point += best_sushi[i]
    if len(other_sushi) == 0:
        break
    rem = other_sushi.pop()  # 取り除く寿司
    sushi_point -= rem
    kind_point = (i + 1) ** 2

    if ans < sushi_point + kind_point:
        ans = sushi_point + kind_point

print(ans)
