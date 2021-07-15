for i in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    h, w = y2 - y1, x2 - x1
    print(h * w + 1)
