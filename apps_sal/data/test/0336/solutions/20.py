
def __starting_point():
    #n, m = list(map(int, input().split()))
    n, a, b, c, d = list(map(int, input().split()))
    x = max([1 - a + d, 1 - b + c, 1, 1 - a - b + d + c])
    y = min([n - a + d, n - b + c, n, n - a - b + d + c])
    #print(x, y)
    if x > y:
        print(0)
        return
    else:
        print(n * (y - x + 1))


__starting_point()
