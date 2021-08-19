def __starting_point():
    (l, r) = [int(__) for __ in input().strip().split()]
    print('YES')
    while l <= r:
        print(l, l + 1)
        l += 2


__starting_point()
