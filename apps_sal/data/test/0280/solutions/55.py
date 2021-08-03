from bisect import bisect_left
from itertools import permutations

N, M = map(int, input().split())
w = list(map(int, input().split()))
lv = [list(map(int, input().split())) for i in range(M)]

# 注目すべき橋だけ取り出す
lv.sort(key=lambda x: x[1])
l = [0]
v = [0]
for li, vi in lv:
    if vi == v[-1]:
        l[-1] = max(l[-1], li)
    elif li > l[-1]:
        l.append(li)
        v.append(vi)

# 耐荷重を単体で超えるラクダがいる場合は渡れない
if v[1] < max(w):
    print(-1)
    return

# 順序を固定したときの距離を計算


def solve(order):
    x = [-1] * N
    x[0] = 0
    for i in range(1, N):
        w_now = order[i]
        for j in range(i - 1, -1, -1):
            w_now += order[j]
            space = l[bisect_left(v, w_now) - 1]
            x[i] = max(x[i], x[j] + space)
    return x[-1]


# ラクダの並べ替えを全て試す
ans = float('inf')
for order in permutations(w):
    ans = min(ans, solve(order))

print(ans)
