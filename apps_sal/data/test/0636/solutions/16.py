from operator import itemgetter
__author__ = 'Konrad Strack'


def solve():
    (n, k) = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    indexed = [(i + 1, x) for (i, x) in enumerate(a)]
    sum = 0
    selected = []
    for (i, v) in sorted(indexed, key=itemgetter(1)):
        if sum + v <= k:
            sum += v
            selected.append(str(i))
        else:
            break
    print(len(selected))
    if len(selected) > 0:
        print(' '.join(selected))


def __starting_point():
    solve()


__starting_point()
