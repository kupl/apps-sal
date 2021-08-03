"""
5
1 4
2 5
3 1
4 5
"""

n = int(input())


d = dict()
point = dict()
l = []
for _ in range(n - 1):
    l += [list(map(int, input().split()))]


def get_point(nn):
    i = nn
    while not point[i] == i:
        i = point[i]
    return i


for pair in l:
    p0 = pair[0] in list(point.keys())
    p1 = pair[1] in list(point.keys())
    if not (p0 or p1):
        point[pair[1]] = pair[0]
        point[pair[0]] = pair[0]
        d[pair[0]] = [pair[0], pair[1]]
    elif p0 and not p1:
        pp = get_point(pair[0])
        d[pp] += [pair[1]]
        point[pair[1]] = pp
    elif p1 and not p0:
        pp = get_point(pair[1])
        d[pp] += [pair[0]]
        point[pair[0]] = pp
    else:
        pp1 = get_point(pair[1])
        pp0 = get_point(pair[0])
        d[pp0] += d[pp1]
        point[pp1] = pp0

print(' '.join(map(str, d[get_point(1)])))
