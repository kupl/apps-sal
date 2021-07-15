
def lucky(s):
    ds = []

    while s:
        ds.append(s % 10)
        s //= 10

    while len(ds) < 6:
        ds.append(0)


    return ds[0] + ds[1] + ds[2] == ds[3] + ds[4] + ds[5]


def difs(a, b):
    d = 0

    while a or b:
        if a % 10 != b % 10:
            d += 1

        a //= 10
        b //= 10

    return d


def main():
    s = int(input())

    min_difs = 10
    end = 10 ** 6

    for s_t in range(0, end):
        if lucky(s_t):
#            import pdb; pdb.set_trace()
            min_difs = min(min_difs, difs(s, s_t))
            
            if min_difs == 0:
                break

    print(min_difs)


def __starting_point():
    main()





__starting_point()
