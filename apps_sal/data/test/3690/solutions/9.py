def getListInt():
    return [int(x) for x in input().split(' ')]


def solution():
    (h, m, s, t1, t2) = getListInt()
    if t2 == min(t1, t2):
        (t1, t2) = (t2, t1)
    m = float(m) / 5
    s = float(s) / 5
    nbrIn = 0
    if s > t1 and s < t2:
        nbrIn += 1
    if m > t1 and m < t2 or (m == t1 and s != 0):
        nbrIn += 1
    if h > t1 and h < t2 or (h == t1 and (m != 0 or s != 0)):
        nbrIn += 1
    return nbrIn == 0 or nbrIn == 3


print('YES' if solution() else 'NO')
