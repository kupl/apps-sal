def main():
    n = int(input())
    xym, xyM, x_ym, x_yM = 10**9, -10**9, 10**9, -10**9
    for _ in range(n):
        x, y = map(int, input().split())
        xy, x_y = x+y, x-y
        xym, xyM, x_ym, x_yM = min(xym, xy), max(xyM, xy), min(x_ym, x_y), max(x_yM, x_y)
    print(max(xyM-xym, x_yM-x_ym))

def __starting_point():
    main()
__starting_point()
