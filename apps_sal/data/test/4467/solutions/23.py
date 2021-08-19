n = int(input())
cr = [tuple(map(int, input().split())) for _ in range(n)]
cb = [tuple(map(int, input().split())) for _ in range(n)]
cb.sort(key=lambda xy: xy[0])
cr.sort(key=lambda xy: xy[1], reverse=True)
npair = 0
for (bx, by) in cb:
    for (rx, ry) in cr:
        if rx < bx and ry < by:
            npair += 1
            cr.remove((rx, ry))
            break
print(npair)
