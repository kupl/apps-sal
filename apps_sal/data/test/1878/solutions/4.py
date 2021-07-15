def __starting_point():
    n = int(input())
    total = 0
    for i in range(n):
        x1, y1, x2, y2 = map(int, input().split())
        w = abs(x1 - x2) + 1
        h = abs(y1 - y2) + 1
        total += w * h

    print(total)
__starting_point()
