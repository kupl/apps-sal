import itertools


def enum(a):
    t = [0]
    for a1, a2 in itertools.combinations(a, 2):
        t.append(a1[0] - a2[0])
        t.append(a2[0] - a1[0])
        t.append((a1[0] - a2[0]) / 2)
        t.append((a2[0] - a1[0]) / 2)
    return t


def calcWidth(l, t):
    x_min = x_max = l[0][0] + l[0][1] * t
    for item in l:
        x_min = min(x_min, item[0] + item[1] * t)
        x_max = max(x_max, item[0] + item[1] * t)
    return x_max - x_min


def calc(x_trip, y_trip, t):
    if t < 0:
        return calcWidth(x_trip, 0) * calcWidth(y_trip, 0)
    return calcWidth(x_trip, t) * calcWidth(y_trip, t)


n = int(input())
x_r, x_n, x_l = [], [], []
y_u, y_n, y_d = [], [], []
for _ in range(n):
    x, y, d = input().strip().split()
    x, y = int(x), int(y)
    if d == "R":
        x_r.append(x)
    elif d == "L":
        x_l.append(x)
    else:
        x_n.append(x)

    if d == "U":
        y_u.append(y)
    elif d == "D":
        y_d.append(y)
    else:
        y_n.append(y)

x_r.sort()
x_n.sort()
x_l.sort()
y_u.sort()
y_n.sort()
y_d.sort()


def ht(x, d):
    if len(x) > 0:
        return [(x[0], d), (x[-1], d)]
    return []


x_list = ht(x_r, 1) + ht(x_n, 0) + ht(x_l, -1)
y_list = ht(y_u, 1) + ht(y_n, 0) + ht(y_d, -1)
t = enum(x_list + y_list)

ans = calc(x_list, y_list, 0)
for t1 in t:
    if t1 < 0:
        continue
    wx = calcWidth(x_list, t1)
    wy = calcWidth(y_list, t1)
    ans = min(ans, calc(x_list, y_list, t1))
    ans = min(ans, calc(x_list, y_list, t1 + (wx - wy) / 2))
    ans = min(ans, calc(x_list, y_list, t1 + (wy - wx) / 2))
    ans = min(ans, calc(x_list, y_list, t1 + (wx * 2 - wy) / 4))
    ans = min(ans, calc(x_list, y_list, t1 + (wx - wy * 2) / 4))
    ans = min(ans, calc(x_list, y_list, t1 + (wy * 2 - wx) / 4))
    ans = min(ans, calc(x_list, y_list, t1 + (wy - wx * 2) / 4))
    ans = min(ans, calc(x_list, y_list, t1 + (wx * 2 - wy * 2) / 8))
    ans = min(ans, calc(x_list, y_list, t1 + (wy * 2 - wx * 2) / 8))
print(ans)
