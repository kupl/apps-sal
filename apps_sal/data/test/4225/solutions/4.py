def __starting_point():
    S = input()
    (a, b, c, k) = map(int, S.split(sep=' '))
    if k <= a:
        print(k)
    elif k <= a + b:
        print(a)
    elif k <= a + b + c:
        print(a - (k - a - b))


__starting_point()
