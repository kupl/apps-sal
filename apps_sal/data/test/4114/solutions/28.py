N = int(input())
hyx = [list(map(int, input().split()))[::-1] for _ in range(N)]
R = range(101)
for X in R:
    for Y in R:
        (h, y, x) = max(hyx)
        H = h + abs(X - x) + abs(Y - y)
        if all((h == max(H - abs(X - x) - abs(Y - y), 0) for (h, y, x) in hyx)):
            print(X, Y, H)
