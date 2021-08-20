def main():
    (c1, c2, c3, c4) = list(map(int, input().split()))
    input()
    aa = list(map(int, input().split()))
    bb = list(map(int, input().split()))
    t = c2 // c1
    (c5, c6) = (sum((c1 * x if x <= t else c2 for x in l)) for l in (aa, bb))
    print(min(c3 * 2, c3 + c5, c3 + c6, c5 + c6, c4))


def __starting_point():
    main()


__starting_point()
