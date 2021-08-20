import sys
3
MAPPING = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}


def read_ints():
    return [int(x) for x in input().split()]


def get_vectors(moves):
    vector = (0, 0)
    yield vector
    for move in moves:
        delta = MAPPING[move]
        vector = (vector[0] + delta[0], vector[1] + delta[1])
        yield vector


def mul(pair, a):
    return (pair[0] * a, pair[1] * a)


def is_achievable(diff, period):
    if diff == (0, 0):
        return True
    if period == (0, 0):
        return False
    if period[0] != 0:
        if diff[0] % period[0] == 0:
            times = diff[0] // period[0]
            if times > 0 and mul(period, times) == diff:
                return True
    if period[1] != 0:
        if diff[1] % period[1] == 0:
            times = diff[1] // period[1]
            if times > 0 and mul(period, times) == diff:
                return True
    return False


def main():
    (a, b) = read_ints()
    moves = input().strip()
    vectors = list(get_vectors(moves))
    period = vectors[-1]
    for vector in vectors:
        diff = (a - vector[0], b - vector[1])
        if is_achievable(diff, period):
            print('Yes')
            return
    print('No')


def __starting_point():
    main()


__starting_point()
