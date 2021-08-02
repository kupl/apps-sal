x, y = map(int, input().split())

isCorner = (x == y) or (-x == y and y > 0) or (y == -x + 1 and x is not 0)


reachX = (0 if x == 0 else 1 + (x - 1) * 4 if x > 0 else 3 + (abs(x) - 1) * 4)
reachY = (0 if y == 0 else 2 + (y - 1) * 4 if y > 0 else abs(y) * 4)
if isCorner:
    print(min(reachX, reachY))
else:
    print(max(reachX, reachY))
