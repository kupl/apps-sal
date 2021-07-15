vertical1, horizontal1, vertical2, horizontal2 = map(int, input().split())
area1 = vertical1 * horizontal1
area2 = vertical2 * horizontal2
if area1 < area2:
    print(area2)
else:
    print(area1)
