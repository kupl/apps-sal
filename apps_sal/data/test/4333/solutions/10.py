import sys
read = sys.stdin.read
readlines = sys.stdin.readlines


def main():
    x1, y1, x2, y2 = map(int, input().split())
    diff_x = x2 - x1
    diff_y = y2 - y1
    r = [x2 - diff_y, y2 + diff_x, x1 - diff_y, y1 + diff_x]
    print(*r, sep=' ')


def __starting_point():
    main()


__starting_point()
