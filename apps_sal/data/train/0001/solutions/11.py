USE_STDIO = False

if not USE_STDIO:
    try:
        import mypc
    except:
        pass


def main():
    q, = list(map(int, input().split(' ')))
    for _ in range(q):
        n, m, k = list(map(int, input().split(' ')))
        if n > k or m > k:
            print(-1)
        elif (n - m) % 2:
            print(k - 1)
        elif (n - k) % 2:
            print(k - 2)
        else:
            print(k)


def __starting_point():
    main()


__starting_point()
