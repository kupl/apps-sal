def main():

    def center(xx):
        return (sum(xx[::2]) * 0.25, sum(xx[1::2]) * 0.25)
    aa = list(map(float, input().split()))
    bb = list(map(float, input().split()))
    (x, y) = center(aa)
    for i in range(0, 8, 2):
        aa[i] -= x
        bb[i] -= x
        aa[i + 1] -= y
        bb[i + 1] -= y
    (x, y) = center(bb)
    if x < 0.0:
        for i in range(0, 8, 2):
            bb[i] *= -1.0
    if y < 0.0:
        for i in range(1, 8, 2):
            bb[i] *= -1.0
    (x, y) = max((aa[i:i + 2] for i in range(0, 8, 2)))
    for i in range(0, 8, 2):
        bb[i] -= x
        bb[i + 1] -= y
    ([x1, y1], [x2, y2]) = sorted((bb[i:i + 2] for i in range(0, 8, 2)))[:2]
    print(('NO', 'YES')[x1 <= 0 and x1 + y1 <= 0.0 and (y2 <= 0.0) and (x2 + y2 <= 0.0)])


def __starting_point():
    main()


__starting_point()
