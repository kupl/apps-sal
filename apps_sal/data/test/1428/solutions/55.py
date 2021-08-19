from collections import Counter
from itertools import permutations
(n, c) = list(map(int, input().split()))
d = [list(map(int, input().split())) for _ in range(c)]
ci = [[] for _ in range(3)]
for i in range(n):
    cl = list(map(int, input().split()))
    for j in range(3):
        ci[(i + j) % 3].extend(cl[j::3])
for i in range(3):
    ci[i] = Counter(ci[i])


def iwa(cols):
    ret = 0
    for i in range(3):
        for (x, v) in list(ci[i].items()):
            ret += v * d[x - 1][cols[i]]
    return ret


L = list(permutations(list(range(c)), 3))
ret = 500 * 500 * 1000
for cols in L:
    ret = min(ret, iwa(cols))
print(ret)
