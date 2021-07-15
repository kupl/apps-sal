for tc in range(int(input())):
    mainFlag = False
    pairFlag = False
    n, m = map(int, input().split())
    tiles = set()
    for _ in range(n):
        a, b = map(int, input().split())
        c, d = map(int, input().split())
        tile = (a, b, c, d)
        tiles.add(tile)
        if b == c:
            mainFlag = True
            pairFlag = True
        if (a, c, b, d) in tiles:
            pairFlag = True
    if mainFlag and pairFlag and m % 2 == 0:
        print("YES")
    else:
        print("NO")
