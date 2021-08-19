from bisect import bisect_left, bisect_right
n = int(input())
al = list(map(int, input().split()))
al.sort()
ai = al[-1]
if ai % 2 == 0:
    aj_best = ai // 2
    ind = bisect_right(al, aj_best) - 1
    ind = ind if 0 <= ind < n else None
    val1 = al[ind] if ind is not None else 0
    ind = bisect_left(al, aj_best)
    ind = ind if 0 <= ind < n else None
    val2 = al[ind] if ind is not None else ai
    if abs(aj_best - val1) <= abs(aj_best - val2):
        aj = val1
    else:
        aj = val2
else:
    aj_best = ai // 2
    ind = bisect_right(al, aj_best) - 1
    ind = ind if 0 <= ind < n else None
    val1 = al[ind] if ind is not None else 0
    ind = bisect_left(al, aj_best)
    ind = ind if 0 <= ind < n else None
    val2 = al[ind] if ind is not None else ai
    if abs(aj_best - val1) <= abs(aj_best + 1 - val2):
        aj = val1
    else:
        aj = val2
print(ai, aj)
