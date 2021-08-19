t = int(input())
while t > 0:
    (x1, y1, x2, y2) = map(int, input().split())
    print((x2 - x1) * (y2 - y1) + 1)
    t -= 1
