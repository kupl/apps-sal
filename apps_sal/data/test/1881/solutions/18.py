def main():
    (n, k) = [int(_) for _ in input().split()]
    a = [int(_) for _ in input().split()]
    p = [-1] * 256
    p[0] = 0
    for x in a:
        if p[x] < 0:
            for y in range(x - 1, max(-1, x - k), -1):
                if p[y] >= 0:
                    if p[y] + k > x:
                        p[x] = p[y]
                    else:
                        p[x] = p[y + 1] = y + 1
                    break
            if p[x] < 0:
                p[x] = p[x - k + 1] = x - k + 1
    b = [p[x] for x in a]
    print(' '.join(map(str, b)))


def __starting_point():
    main()


__starting_point()
