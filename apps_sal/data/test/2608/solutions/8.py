def get_colors(x1, y1, x2, y2):
    w = x2 - x1 + 1
    h = y2 - y1 + 1
    if w % 2 == 0 or h % 2 == 0:
        black = w * h // 2
        white = w * h // 2
    else:
        oddx = w // 2
        if x1 % 2 == 1 and x2 % 2 == 1:
            oddx += 1
        oddy = h // 2
        if y1 % 2 == 1 and y2 % 2 == 1:
            oddy += 1
        evenx = w // 2
        if x1 % 2 == 0 and x2 % 2 == 0:
            evenx += 1
        eveny = h // 2
        if y1 % 2 == 0 and y2 % 2 == 0:
            eveny += 1
        white = oddx * oddy + evenx * eveny
        black = w * h - white
    return white, black

def get_intersection(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    if ax1 > bx2:
        return None, None, None, None
    if bx1 > ax2:
        return None, None, None, None
    if ay1 > by2:
        return None, None, None, None
    if by1 > ay2:
        return None, None, None, None
    return max(ax1, bx1), max(ay1, by1), min(ax2, bx2), min(ay2, by2)

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    white, black = get_colors(1, 1, m, n)
    wx1, wy1, wx2, wy2 = map(int, input().split())
    w, b = get_colors(wx1, wy1, wx2, wy2)
    white += b
    black -= b
    bx1, by1, bx2, by2 = map(int, input().split())
    ix1, iy1, ix2, iy2 = get_intersection(wx1, wy1, wx2, wy2, bx1, by1, bx2, by2)
    if ix1 is not None:
        w, b = get_colors(ix1, iy1, ix2, iy2)
        white -= b
        black += b
    w, b = get_colors(bx1, by1, bx2, by2)
    white -= w
    black += w
    print(white, black)
