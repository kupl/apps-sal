def dist(x1, x2, y1, y2):
    return (x1 - x2)**2 + (y1 - y2)**2


ax, ay, bx, by, cx, cy = map(int, input().split())
if ((by - ay) * (cx - bx) == (cy - by) * (bx - ax)):
    print('No')
else:
    if(dist(ax, bx, ay, by) == dist(bx, cx, by, cy)):
        print('Yes')
    else:
        print('No')
