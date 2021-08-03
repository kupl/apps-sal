def black_count(x, y):
    total = x * y
    return total // 2


def black_count2(a, b, c, d):
    return black_count(c, d) - black_count(a - 1, d) - black_count(c, b - 1) + black_count(a - 1, b - 1)


def white_count2(a, b, c, d):
    total = (c - a + 1) * (d - b + 1)
    return total - black_count2(a, b, c, d)


def intersection(a, b, c, d, x, y):
    if x < a or y < b:
        return None
    x = min(x, c)
    y = min(y, d)
    return (a, b, x, y)


def intersection2(a1, b1, c1, d1, a2, b2, c2, d2):
    if b1 > d2 or a1 > c2:
        return None
    if b2 > d1 or a2 > c1:
        return None

    a = max(a1, a2)
    b = max(b1, b2)
    c = min(c1, c2)
    d = min(d1, d2)
    return (a, b, c, d)


def solve(n, m, W, B):
    total = n * m
    whites = total - black_count(n, m)
    whites += black_count2(*W)
    whites -= white_count2(*B)
    I = intersection2(*W, *B)
    if I:
        whites -= black_count2(*I)
    blacks = n * m - whites
    return whites, blacks


def main():
    t = int(input())
    for _ in range(t):
        n, m = list(map(int, input().split()))
        W = list(int(i) for i in input().split())
        B = list(int(i) for i in input().split())
        w, b = solve(n, m, W, B)
        print(w, b)


def __starting_point():
    main()


__starting_point()
