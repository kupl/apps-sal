import operator
import itertools


def count_inversions(ns):

    return sum(itertools.starmap(operator.gt, itertools.combinations(ns, 2)))


def rotate(ns, l, r):

    return ns[:l] + ns[l:r + 1][::-1] + ns[r + 1:]


def rotate_times(ns, k):

    if k == 0:

        yield ns

    else:

        for l, r in itertools.combinations_with_replacement(list(range(len(ns))), 2):

            yield from rotate_times(rotate(ns, l, r), k - 1)


n, k = list(map(int, str.split(input())))
ns = tuple(map(int, str.split(input())))
inv = tuple(map(count_inversions, rotate_times(ns, k)))
print(sum(inv) / len(inv))
