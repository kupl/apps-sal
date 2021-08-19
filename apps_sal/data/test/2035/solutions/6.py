import math


def main():
    (n, xs, ys) = tuple([int(x) for x in input().split()])
    p1 = 0
    p2 = 0
    p3 = 0
    p4 = 0
    for i in range(n):
        (x, y) = tuple([int(x) for x in input().split()])
        if x < xs:
            p1 += 1
        if x > xs:
            p2 += 1
        if y < ys:
            p3 += 1
        if y > ys:
            p4 += 1
    p = max(p1, p2, p3, p4)
    print(p)
    best = []
    if p1 == p:
        best = [xs - 1, ys]
    elif p2 == p:
        best = [xs + 1, ys]
    elif p3 == p:
        best = [xs, ys - 1]
    else:
        best = [xs, ys + 1]
    print(' '.join([str(x) for x in best]))


def __starting_point():
    main()


__starting_point()
