def stessocolore(x1,y1,x2,y2):
    if (x1+y1)%2 == (x2+y2)%2:
        return True
    else:
        return False
x1, y1, x2, y2 = map(int, input().split())
if x1 == x2 or y1 == y2:
    rook = 1
else:
    rook = 2
king = max([abs(x1-x2),abs(y1-y2)])
if stessocolore(x1,y1,x2,y2):
    if (x1-y1) == (x2-y2) or x1+y1 == x2+y2:
        bish = 1
    else:
        bish = 2
else:
    bish = 0

print(rook, bish, king)
