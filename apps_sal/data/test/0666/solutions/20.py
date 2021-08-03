

def __starting_point():
    n = int(input())
    res = ((-1) + (((8 * n) + 1)**(1 / 2))) / 2
    if res == int(res) / 1:
        print(int(res))
    else:
        k = int(res)
        k = (k * (k + 1)) // 2
        p = n - k
        print(p)


__starting_point()
