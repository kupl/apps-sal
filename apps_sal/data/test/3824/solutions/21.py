(x1, y1) = list(map(int, input().split()))
(x2, y2) = list(map(int, input().split()))
if x1 == x2:
    print(4 + (abs(y2 - y1) + 1) * 2)
elif y1 == y2:
    print((abs(x2 - x1) + 1) * 2 + 4)
else:
    print((abs(x2 - x1) + 1) * 2 + (abs(y2 - y1) + 1) * 2)
