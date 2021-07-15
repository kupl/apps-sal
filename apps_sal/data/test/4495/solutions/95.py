def __starting_point():
    a, b, x = map(int, input().split())
    l = b // x
    r = (a-1) // x
    print(l - r)
__starting_point()
