USE_STDIO = False

if not USE_STDIO:
    try:
        import mypc
    except:
        pass


def main():
    n, m = list(map(int, input().split(' ')))
    if m == 0:
        print(n, n)
        return

    minc = max(0, n - m * 2)

    x = int((m * 2)**0.5)
    if x * (x + 1) < m * 2:
        x += 1
    maxc = n - (x + 1)

    print(minc, maxc)


def __starting_point():
    main()


__starting_point()
