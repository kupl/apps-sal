USE_STDIO = False
if not USE_STDIO:
    try:
        import mypc
    except:
        pass


def main():
    (n, k) = list(map(int, input().split(' ')))
    minx = max(1, k - n)
    maxx = min(n, (k - 1) // 2)
    if minx > maxx:
        print(0)
    else:
        print(maxx - minx + 1)


def __starting_point():
    main()


__starting_point()
