import sys
from itertools import permutations
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

N, M = list(map(int, input().split()))
w = list(map(int, input().split()))
lv = [tuple(map(int, input().split())) for _ in range(M)]


def solve(w, lv):
    # どのようにしても橋が崩落してしまう
    if max(w) > min(_[1] for _ in lv):
        return -1

    # 前処理
    lv.sort(key=lambda x: x[1])
    vs = []
    ls = []
    for l, v in lv:
        if len(ls) == 0 or l > ls[-1]:
            vs.append(v)
            ls.append(l)

    ans = -2
    # ラクダたちの隊列を全探索
    for p in permutations(w):
        cum_weights = [0]
        positions = [0]
        for i, wi in enumerate(p):
            cum_weights.append(cum_weights[-1] + wi)
            if i == 0:
                continue

            next_pos = positions[-1]
            for j in range(i):
                intarval_weight = cum_weights[i + 1] - cum_weights[j]
                critical_bridge = bisect_left(vs, intarval_weight) - 1
                if critical_bridge >= 0:
                    next_pos = max(next_pos, positions[j] + ls[critical_bridge])

            positions.append(next_pos)

        if ans == -2:
            ans = positions[-1]
        else:
            ans = min(ans, positions[-1])
    return ans


print((solve(w, lv)))
