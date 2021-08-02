def man_dist(a1, a2, b1, b2):
    return int(abs(a1 - b1) + abs(a2, b2))


def print_md(ax, ay, bx, by):
    ret = []
    if ax > bx:
        xz = ax
        yz = ay
        ax = bx
        ay = by
        bx = xz
        by = yz
    for i in range(ax + 1, bx):
        ret.append([i, min(ay, by)])
    if ay > by:
        z = ax
    else:
        z = bx
    for j in range(min(ay, by) + 1, max(ay, by)):
        ret.append([z, j])
    if ay > by:
        ret.append([ax, by])
    else:
        ret.append([bx, ay])
    return ret


xa, ya = list(map(int, input().split()))
xb, yb = list(map(int, input().split()))
xc, yc = list(map(int, input().split()))
if max(xb, xc) > xa > min(xb, xc) and max(yb, yc) > ya > max(yb, yc):
    print(man_dist(xc, yc, xb, yb) - 2)
    ans = []
    for i in print_md(xb, yb, xa, ya):
        ans.append(i)
    for i in print_md(xa, ya, xc, yc):
        if ans.count(i) == 0:
            ans.append(i)
elif max(xa, xc) > xb > min(xa, xc) and max(ya, yc) > yb > max(ya, yc):
    print(man_dist(xa, ya, xc, yc) - 2)
    xz = xa
    yz = ya
    xa = xb
    ya = yb
    xb = xz
    yb = yz
    ans = []
    for i in print_md(xb, yb, xa, ya):
        ans.append(i)
    for i in print_md(xa, ya, xc, yc):
        if ans.count(i) == 0:
            ans.append(i)
elif max(xa, xb) > xc > min(xa, xb) and max(ya, yb) > yc > max(ya, yb):
    print(man_dist(xa, ya, xb, yb) - 2)
    xz = xa
    yz = ya
    xa = xc
    ya = yc
    xc = xz
    yc = yz
    ans = []
    for i in print_md(xb, yb, xa, ya):
        ans.append(i)
    for i in print_md(xa, ya, xc, yc):
        if ans.count(i) == 0:
            ans.append(i)
else:
    if yb < yc and yb < ya:
        xz = xb
        yz = yb
        xb = xc
        yb = yc
        xc = xz
        yc = yz
    elif ya < yc and ya < yb:
        xz = xa
        yz = ya
        xa = xc
        ya = yc
        xc = xz
        yc = yz
    ans = print_md(xa, ya, xb, yb)
    if xc < min(xa, xb):
        for i in print_md(xc, yc, min(xa, xb), min(ya, yb)):
            if ans.count(i) == 0:
                ans.append(i)
    elif xc > max(xa, xb):
        for i in print_md(xc, yc, max(xa, xb), min(ya, yb)):
            if ans.count(i) == 0:
                ans.append(i)
    else:
        for i in print_md(xc, yc, xc, min(ya, yb)):
            if ans.count(i) == 0:
                ans.append(i)
if ans.count([xa, ya]) == 0:
    ans.append([xa, ya])
if ans.count([xb, yb]) == 0:
    ans.append([xb, yb])
if ans.count([xc, yc]) == 0:
    ans.append([xc, yc])
print(len(ans))
for i in ans:
    print(i[0], i[1])
