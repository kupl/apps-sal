from collections import deque
from sys import stdin
lines = deque(line.strip() for line in stdin.readlines())


def nextline():
    return lines.popleft()


def types(cast, sep=None):
    return tuple(cast(x) for x in strs(sep=sep))


def ints(sep=None):
    return types(int, sep=sep)


def strs(sep=None):
    return tuple(nextline()) if sep == '' else tuple(nextline().split(sep=sep))


def intersect(s1, s2):
    if s1[0] >= s2[0] and s1[0] <= s2[1]:
        return s1[0], min(s1[1], s2[1])
    if s2[0] >= s1[0] and s2[0] <= s1[1]:
        return s2[0], min(s1[1], s2[1])
    return 0, 0


def get_len(segment):
    return segment[1] - segment[0]


def main():
    # lines will now contain all of the input's lines in a list
    N = int(nextline())
    segments = list(ints() for _ in range(N))
    forwards = [segments[0]]
    backwards = [segments[-1]]
    for i in range(1, N):
        forwards.append(intersect(forwards[-1], segments[i]))
        backwards.append(intersect(backwards[-1], segments[~i]))
    backwards = backwards[::-1]
    maxlen = max(get_len(forwards[-2]), get_len(backwards[1]))
    for i in range(1, N - 1):
        maxlen = max(maxlen, get_len(intersect(forwards[i - 1], backwards[i + 1])))
    print(maxlen)


def __starting_point():
    main()


__starting_point()
