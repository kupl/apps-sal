USE_STDIO = False
if not USE_STDIO:
    try:
        import mypc
    except:
        pass


def main():
    (n, k) = list(map(int, input().split(' ')))
    ans = (k + n - 1) // n
    print(ans)


def __starting_point():
    main()


__starting_point()
