def main():
    x1, y1, x2, y2 = list(map(int, input().split()))
    x, y = list(map(int, input().split()))

    if abs(x2 - x1) % x or abs(y2 - y1) % y:
        print('NO')
        return

    if (abs(x2 - x1) // x + abs(y2 - y1) // y) % 2 == 0:
        print('YES')
    else:
        print('NO')


main()
