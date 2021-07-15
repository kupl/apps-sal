from itertools import chain


def main():
    n = int(input())
    aa = list(map(int, input()))
    res = []
    for j in range(len(aa)):
        y, base = 0, aa[j]
        for x in chain(aa[j:], aa[:j]):
            y = y * 10 + (x - base) % 10
        res.append(y)
    f = str(len(aa)).join(('{:0>', 'd}'))
    print(f.format(min(res)))


def __starting_point():
    main()
__starting_point()
