from itertools import accumulate
from itertools import product

D, G = list(map(int, input().split()))
points = []
for i, _ in enumerate(list(range(D)), 1):
    P, C = list(map(int, input().split()))
    point = list(accumulate([100 * i] * P))
    point[-1] += C
    points.append(point)

# 中途半端に解く問題は1問だけ。解くなら高得点ほど良い。
ans = 1000
for completes in product(list(range(2)), repeat=D):
    solves = 0
    total = 0
    ex_points = []
    for comp, point in zip(completes, points):
        if comp:
            total += point[-1]
            solves += len(point)
        else:
            ex_points = point

    # 目標に届かない場合、高配点を追加で解く
    if total < G:
        for i, p in enumerate(ex_points, 1):
            if total + p >= G:
                # 目標に届いた
                solves += i
                break
        else:
            # 目標に届かない
            continue

    ans = min(ans, solves)

print(ans)
