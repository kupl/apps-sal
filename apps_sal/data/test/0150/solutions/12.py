def main():
    from math import sqrt
    n = int(input())
    if not n & 1:
        print(2 if n > 2 else 1)
        return
    for p in range(3, int(sqrt(n)) + 1, 2):
        if not n % p:
            break
    else:
        print(1)
        return
    n -= 2
    for p in range(3, int(sqrt(n)) + 1, 2):
        if not n % p:
            break
    else:
        print(2)
        return
    print(3)


def __starting_point():
    main()


__starting_point()
