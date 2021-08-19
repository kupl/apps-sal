N = int(input())
xyh = [list(map(int, input().split())) for _ in range(N)]
hxy = [[h, x, y] for (x, y, h) in xyh]
hxy.sort()
for X in range(101):
    for Y in range(101):
        (h, x, y) = hxy[-1]
        H = h + abs(X - x) + abs(Y - y)
        if all((h == max(H - abs(X - x) - abs(Y - y), 0) for (h, x, y) in hxy)):
            print(X, Y, H)
