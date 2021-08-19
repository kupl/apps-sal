from collections import defaultdict
d = defaultdict(int)


def __starting_point():
    input()
    sum_v = 0
    for (i, x) in enumerate(input()):
        if i % 2 == 0:
            d[x] += 1
        elif d[x.lower()] == 0:
            sum_v += 1
        else:
            d[x.lower()] -= 1
    print(sum_v)


__starting_point()
