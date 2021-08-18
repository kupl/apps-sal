

def main():
    n, h, m = list(map(int, input().split()))
    spots = [h] * n
    for _ in range(m):
        l, r, x = list(map(int, input().split()))
        for i in range(l - 1, r):
            spots[i] = min(spots[i], x)
    ret = sum([a ** 2 for a in spots])
    print(ret)


def __starting_point():
    main()


__starting_point()
