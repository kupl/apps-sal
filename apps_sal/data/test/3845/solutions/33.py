def main():
    a, b = map(int, input().split())
    k = 50
    gw = [['.'] * 2 * k for _ in range(k)]
    gb = [['#'] * 2 * k for _ in range(k)]
    for i in range(b - 1):
        h = (i // k) * 2
        w = (i % k) * 2
        gw[h][w] = '#'
    for i in range(a - 1):
        h = (i // k) * 2 + 1
        w = (i % k) * 2 + 1
        gb[-h][-w] = '.'
    ans = gw + gb
    print(2 * k, 2 * k)
    for l in ans:
        print(*l, sep='')


def __starting_point():
    main()


__starting_point()
