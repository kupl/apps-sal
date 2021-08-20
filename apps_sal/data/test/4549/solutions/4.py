import sys
input = sys.stdin.readline
d = '.'
dn = '#'


def isPaintable(h, w, x, y, canvas):
    if x > 0:
        if canvas[y][x - 1] == dn:
            return True
    if x < w - 1:
        if canvas[y][x + 1] == dn:
            return True
    if y > 0:
        if canvas[y - 1][x] == dn:
            return True
    if y < h - 1:
        if canvas[y + 1][x] == dn:
            return True
    return False


def main():
    ans = 'Yes'
    (h, w) = map(int, input().split())
    canvas = []
    for _ in range(h):
        s = list(input().rstrip('\n'))
        canvas.append(s)
    for y in range(h):
        if ans == 'No':
            break
        for x in range(w):
            if canvas[y][x] == dn and (not isPaintable(h, w, x, y, canvas)):
                ans = 'No'
                break
    print(ans)


def __starting_point():
    main()


__starting_point()
