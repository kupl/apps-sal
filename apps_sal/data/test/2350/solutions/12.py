for t in range(int(input())):
    (x1, y1, x2, y2) = list(map(int, input().split()))
    print(1 + (y2 - y1) * (x2 - x1))
