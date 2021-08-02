import sys


def change_rating(div, change):
    if div == 1:
        ranged[0] = max(ranged[0], 1900)
    else:
        ranged[1] = min(ranged[1], 1899)
    if ranged[0] > ranged[1]:
        return False
    ranged[0] += change
    ranged[1] += change
    return True


def get_max_cur(start):
    t = start
    m = start
    for change in reversed(changes):
        m = max(m, start - change)
        start -= change
    if m >= inf:
        return m
    return t


n = int(input())
inf = sys.maxsize * 2000
ranged = [-inf, inf]
changes = []
for _ in range(n):
    chnage, div = list(map(int, input().split()))
    if not change_rating(div, chnage):
        print('Impossible')
        return
    changes.append(chnage)
max_r = get_max_cur(ranged[1])
if max_r >= inf:
    print('Infinity')
else:
    print(max_r)
