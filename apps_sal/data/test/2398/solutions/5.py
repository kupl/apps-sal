def solve():
    (a, b, c, d) = map(int, input().split())
    (x, y, x1, y1, x2, y2) = map(int, input().split())
    dx = b - a
    dy = d - c
    if x1 == x2:
        if a + b:
            print('No')
            return
    if y1 == y2:
        if c + d:
            print('No')
            return
    if x1 <= x + dx <= x2 and y1 <= y + dy <= y2:
        print('Yes')
    else:
        print('No')


def __starting_point():
    t = int(input())
    for _ in range(t):
        solve()


__starting_point()
