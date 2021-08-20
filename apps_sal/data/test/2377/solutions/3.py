import sys
read = sys.stdin.read


def main():
    (n, h, *ab) = list(map(int, read().split()))
    tops = max(ab[0::2])
    tlst = [b for b in ab[1::2] if b > tops]
    tlst.sort(reverse=True)
    i = -1
    t = 0
    for (i, t) in enumerate(tlst):
        h -= t
        if h <= 0:
            h = 0
            break
    print(h // tops + (h % tops > 0) + i + 1)


def __starting_point():
    main()


__starting_point()
