def rotateClk(x, y, n):
    tmp = x
    x = y
    y = n + 1 - tmp
    return (x, y)


def rev(x, y, m):
    return (x, m + 1 - y)


(n, m, x, y, z, p) = [int(x) for x in input().split()]
pts = []
for _ in range(p):
    pts.append([int(x) for x in input().split()])
x = x % 4
y = y % 2
z = z % 4
for (i, pt) in enumerate(pts):
    if x == 1:
        pt = rotateClk(pt[0], pt[1], n)
    elif x == 2:
        pt = rotateClk(pt[0], pt[1], n)
        pt = rotateClk(pt[0], pt[1], m)
    elif x == 3:
        pt = rotateClk(pt[0], pt[1], n)
        pt = rotateClk(pt[0], pt[1], m)
        pt = rotateClk(pt[0], pt[1], n)
    pts[i] = pt
for (i, pt) in enumerate(pts):
    if y == 1:
        pts[i] = rev(pt[0], pt[1], m if x % 2 == 0 else n)
for (i, pt) in enumerate(pts):
    if z == 3:
        pt = rotateClk(pt[0], pt[1], n if x % 2 == 0 else m)
    elif z == 2:
        prev = n if x % 2 == 0 else m
        pt = rotateClk(pt[0], pt[1], prev)
        pt = rotateClk(pt[0], pt[1], n if prev == m else m)
    elif z == 1:
        prev = n if x % 2 == 0 else m
        pt = rotateClk(pt[0], pt[1], prev)
        pt = rotateClk(pt[0], pt[1], n if prev == m else m)
        pt = rotateClk(pt[0], pt[1], prev)
    pts[i] = pt
for pt in pts:
    print(pt[0], pt[1])
