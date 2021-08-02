from itertools import combinations, product
import bisect as bs


def tuple_int(iterable):
    return tuple(map(int, iterable.split()))


def S_with_K_plots(plots, K):
    result = []
    X, Y = sorted([x for x, y in plots]), sorted([y for x, y in plots])
    for xinf, xsup in combinations(X, 2):
        for yinf in Y:
            ysup = [y for x, y in plots if xinf <= x <= xsup and y >= yinf]
            if len(ysup) < K:
                continue
            ysup.sort()
            result.append((xsup - xinf) * (ysup[K - 1] - yinf))
    return result


def __starting_point():
    with open(0) as f:
        N, K = map(int, f.readline().split())
        plots = list(map(tuple_int, f.readlines()))
    print(min(S_with_K_plots(plots, K)))


__starting_point()
