def __starting_point():
    rects = int(input())
    s = 0
    for _ in range(rects):
        x1, y1, x2, y2 = list(map(int, input().split()))
        s += (x2-x1+1) * (y2-y1+1)
    print(s)

__starting_point()
