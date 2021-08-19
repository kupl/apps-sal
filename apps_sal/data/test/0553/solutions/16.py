def main():
    from operator import eq
    (n, l, k) = (int(input()), [], 0)
    if n < 2:
        print(6)
        return
    for _ in range(n):
        a = tuple(input())
        for b in l:
            x = sum(map(eq, a, b))
            if k < x:
                k = x
                if k > 4:
                    print(0)
                    return
        l.append(a)
    print(2 - k // 2)


def __starting_point():
    main()


__starting_point()
