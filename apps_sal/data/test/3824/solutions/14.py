x1, y1 = list(map(int, input().split()))
x2, y2 = list(map(int, input().split()))

if x1 == x2:
    print(4 + 2 * (abs(y2 - y1) + 1))
elif y1 == y2:
    print(4 + 2 * (abs(x2 - x1) + 1))
else:
    print(2 * (abs(x2 - x1) + 1) + 2 * (abs(y2 - y1) + 1))
