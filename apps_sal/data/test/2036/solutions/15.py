n, m, sx, sy = list(map(int, input().split()))


def do_row(sx, vis):
    last = -1
    for j in range(1, m + 1):
        if (sx, j) not in vis:
            print(sx, j)
            vis.add((sx, j))
            last = j
    return last


vis = set()
vis.add((sx, sy))
print(sx, sy)
l = sy
l2 = do_row(sx, vis)
if l2 != -1:
    l = l2
for i in range(1, n + 1):
    if (i, l) in vis:
        continue
    print(i, l)
    vis.add((i, l))
    l2 = do_row(i, vis)
    if l2 != -1:
        l = l2
