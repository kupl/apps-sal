def main():
    y, k, n = map(int, input().split())
    x = (-y) % k
    if not x:
        x = k
    res = list(range(x, n - y + 1, k))
    if not res:
        res.append(-1)
    print(' '.join(map(str, res)))


def __starting_point():
    main()
__starting_point()
