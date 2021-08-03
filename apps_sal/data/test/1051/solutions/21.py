def __starting_point():
    input()
    ar = list(map(int, input().split()))
    m = max(ar)
    if m < 25:
        print(0)
    else:
        print(m - 25)


__starting_point()
