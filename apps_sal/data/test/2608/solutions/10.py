def getBW(x1, y1, x2, y2):
    if (x2 - x1) % 2 == 1 or (y2 - y1) % 2 == 1:
        return [(y2 + 1 - y1) * (x2 + 1 - x1) // 2, (y2 + 1 - y1) * (x2 + 1 - x1) // 2]
    elif x1 % 2 == 0 and y1 % 2 == 0 or (x1 % 2 == 1 and y1 % 2 == 1):
        return [(y2 + 1 - y1) * (x2 + 1 - x1) // 2, 1 + (y2 + 1 - y1) * (x2 + 1 - x1) // 2]
    else:
        return [1 + (y2 + 1 - y1) * (x2 + 1 - x1) // 2, (y2 + 1 - y1) * (x2 + 1 - x1) // 2]


cs = int(input())
for c in range(cs):
    (m, n) = map(int, input().split())
    BW = getBW(1, 1, n, m)
    (x1, y1, x2, y2) = map(int, input().split())
    (x3, y3, x4, y4) = map(int, input().split())
    BW1 = getBW(x1, y1, x2, y2)
    BW2 = getBW(x3, y3, x4, y4)
    BWO = [0, 0]
    xo1 = max(x1, x3)
    xo2 = min(x2, x4)
    yo1 = max(y1, y3)
    yo2 = min(y2, y4)
    if xo2 >= xo1 and yo2 >= yo1:
        BWO = getBW(xo1, yo1, xo2, yo2)
        '\n    print(BW1)\n    print(BW2)\n    print(BWO)\n    print(BW)'
    B = BW[0] - BW1[0] + BW2[1] + BWO[0]
    W = BW[1] + BW1[0] - BW2[1] - BWO[0]
    print(W, end=' ')
    print(B)
