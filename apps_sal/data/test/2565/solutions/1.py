import sys
input = sys.stdin.readline

T = int(input())

for t in range(T):
    x1, y1, z1 = [int(_) for _ in input().split()]
    x2, y2, z2 = [int(_) for _ in input().split()]
    pos_ass = min(z1, y2)
    z1 -= pos_ass
    y2 -= pos_ass
    if y1 > x2 + y2:
        neg_ass = y1 - (x2 + y2)
    else:
        neg_ass = 0
    print(2*(pos_ass-neg_ass))

