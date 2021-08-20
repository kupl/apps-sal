def __starting_point():
    (n, k) = map(int, input().split())
    tmp = n % k
    if n % k == 0:
        print(0)
    else:
        print(1)


__starting_point()
