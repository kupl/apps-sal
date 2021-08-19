import sys
import numpy as np


def sr():
    return sys.stdin.readline().rstrip()


def ir():
    return int(sr())


def lr():
    return list(map(int, sr().split()))


(N, C) = lr()
XV = np.array([lr() for _ in range(N)])
Sushi = XV[:, 1]
Sushi_rev = Sushi[::-1]
dis = XV[:, 0]
dis_rev = C - dis[::-1]
Sushi_cum = Sushi.cumsum()
Sushi_rev_cum = Sushi_rev.cumsum()
Sushi_cum -= dis
Sushi_rev_cum -= dis_rev
Sushi_max = np.maximum.accumulate(Sushi_cum)
Sushi_max_rev = np.maximum.accumulate(Sushi_rev_cum)
answer = max(0, Sushi_max[-1], Sushi_max_rev[-1])
for i in range(N - 1):
    cal = Sushi_cum[i] - dis[i] + Sushi_max_rev[N - 2 - i]
    cal2 = Sushi_rev_cum[i] - dis_rev[i] + Sushi_max[N - 2 - i]
    cal = max(cal, cal2)
    if cal > answer:
        answer = cal
print(answer)
