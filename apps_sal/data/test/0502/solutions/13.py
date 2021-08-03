def readln(): return list(map(int, input().rstrip().split()))


ax, ay, bx, by, cx, cy = readln()
dab = (bx - ax) ** 2 + (by - ay) ** 2
dbc = (cx - bx) ** 2 + (cy - by) ** 2

if dab != dbc:
    print('No')
    return

if (by - ay) * (cx - bx) == (cy - by) * (bx - ax):
    print('No')
    return

print('Yes')
