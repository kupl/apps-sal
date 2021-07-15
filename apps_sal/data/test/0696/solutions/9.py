def main():
    p = int(input())
    if p < 5:
        print(1 )
        return
    res, r = 0, list(range(p - 2))
    for x in range(2, p):
        xx = x
        for _ in r:
            xx %= p
            if xx == 1:
                break
            xx *= x
        else:
            if xx % p == 1:
                res += 1
    print(res)


def __starting_point():
    main()

__starting_point()
