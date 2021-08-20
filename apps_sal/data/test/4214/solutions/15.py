import sys
from itertools import islice, permutations


def resolve(in_):
    N = int(next(in_))
    XY = tuple((tuple(map(int, line.split())) for line in islice(in_, N)))
    count = 0
    distance = 0.0
    for towns in permutations(list(range(N))):
        count += 1
        town0 = towns[0]
        for town1 in towns[1:]:
            (x0, y0) = XY[town0]
            (x1, y1) = XY[town1]
            distance2 = (x1 - x0) ** 2 + (y1 - y0) ** 2
            distance += distance2 ** 0.5
            town0 = town1
    average = distance / count
    return '{:.7f}'.format(average)


def main():
    answer = resolve(sys.stdin)
    print(answer)


def __starting_point():
    main()


__starting_point()
