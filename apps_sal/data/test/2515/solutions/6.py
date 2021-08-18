from math import ceil, sqrt

n = 10**5 + 200
hurui = [i for i in range(n + 1)]
for i in range(2, ceil(sqrt(n)) + 1):
    for j in range(2, ceil(sqrt(i)) + 1):
        if i == 2:
            continue
        if i % j == 0:
            break
    else:
        for k in range(i + i, n, i):
            if hurui[k] != k:
                continue
            hurui[k] = 0
    continue

hurui = [bool(i) for i in hurui]
poi = [False] * (n + 1)
for i in range(n + 1):
    poi[i] = (i % 2 == 1 and hurui[i] and hurui[(i + 1) // 2])
poi[1] = False
sa = [0]
for i in range(n + 1):
    sa.append(sa[i] + poi[i])


q = int(input())
lr = [tuple(map(int, input().split())) for i in range(q)]
for li, ri in lr:
    print((sa[ri + 1] - sa[li]))
