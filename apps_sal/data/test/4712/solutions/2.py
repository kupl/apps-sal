def main():
    (H, W) = list(map(int, input().split()))
    print('#' * (W + 2))
    for _ in range(H):
        print('#{}#'.format(input()))
    print('#' * (W + 2))


def test():
    import doctest
    doctest.testmod()


def __starting_point():
    main()


__starting_point()
