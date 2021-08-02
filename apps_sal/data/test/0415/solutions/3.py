n = int(input())

zi = [int(x) for x in input().split()]


zt = [(0, -1)]


def findmid(g):
    if g <= zt[-1][0]: return
    if g > zt[0][0]: return zt[0][1]
    l = 0
    r = len(zt) - 1
    while l + 1 < r:
        mid = (l + r) // 2
        if g > zt[mid][0]:
            r = mid
        else:
            l = mid
    return zt[r][1]


re = 0
ac = 0
for i in range(n):
    ac += zi[i]
    g = ac - 100 * (i + 1)

    t = findmid(g)
    if t is not None:
        re = max(re, i - t)

    if g < zt[-1][0]:
        zt.append((g, i))


print(re)
