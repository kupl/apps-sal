

def main():
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())
    x5, y5, x6, y6 = map(int, input().split())

    ans = "NO"
    for x in range(x1, x2+1):
        if not (x3 <= x <= x4 and y3 <= y1 <= y4) and not (x5 <= x <= x6 and y5 <= y1 <= y6):
            ans = "YES"
        if not (x3 <= x <= x4 and y3 <= y2 <= y4) and not (x5 <= x <= x6 and y5 <= y2 <= y6):
            ans = "YES"
        if x == x2:
            continue
        x += 0.5
        if not (x3 <= x <= x4 and y3 <= y1 <= y4) and not (x5 <= x <= x6 and y5 <= y1 <= y6):
            ans = "YES"
        if not (x3 <= x <= x4 and y3 <= y2 <= y4) and not (x5 <= x <= x6 and y5 <= y2 <= y6):
            ans = "YES"
        

    for y in range(y1, y2+1):
        if not (x3 <= x1 <= x4 and y3 <= y <= y4) and not (x5 <= x1 <= x6 and y5 <= y <= y6):
            ans = "YES"
        if not (x3 <= x2 <= x4 and y3 <= y <= y4) and not (x5 <= x2 <= x6 and y5 <= y <= y6):
            ans = "YES"
        if y == y2:
            continue
        y += 0.5
        if not (x3 <= x1 <= x4 and y3 <= y <= y4) and not (x5 <= x1 <= x6 and y5 <= y <= y6):
            ans = "YES"
        if not (x3 <= x2 <= x4 and y3 <= y <= y4) and not (x5 <= x2 <= x6 and y5 <= y <= y6):
            ans = "YES"

    print(ans)

def __starting_point():
    main()
__starting_point()
