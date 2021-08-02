n = int(input())
coord = []
for i in range(n):
    coord.append(tuple(list(map(int, input().split())) + [i + 1]))
coord.sort()


def odind(l):
    l.sort()
    for i in range(len(l) // 2):
        print(l[2 * i][-1], l[2 * i + 1][-1])
    if len(l) % 2 == 0:
        return []
    return l[-1]


def dvad(l):
    cx = {}
    ans1 = []
    for x, y, n in l:
        if x in cx:
            cx[x].append([y, n])
        else:
            cx[x] = [[y, n]]
    for x, j in cx.items():
        v = odind(j)
        if len(v) != 0:
            ans1.append(tuple([x] + v))
    ans1.sort()
    for i in range(len(ans1) // 2):
        print(ans1[2 * i][-1], ans1[2 * i + 1][-1])
    if len(ans1) % 2 == 0:
        return []
    return ans1[-1]


def trid(l):
    cx = {}
    ans1 = []
    for x, y, z, n in l:
        if x in cx:
            cx[x].append((y, z, n))
        else:
            cx[x] = [(y, z, n)]
    for x, j in cx.items():
        v = list(dvad(j))
        if len(v) != 0:
            ans1.append(tuple([x] + v))
    ans1.sort()
    for i in range(len(ans1) // 2):
        print(ans1[2 * i][-1], ans1[2 * i + 1][-1])


trid(coord)
