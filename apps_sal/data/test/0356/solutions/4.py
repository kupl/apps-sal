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


def main():
    n = int(nextline())
    a = ints()
    m = int(nextline())
    b = ints()
    count = 1
    i, j = 0, 0
    a_sum, b_sum = 0, 0
    a_total, b_total = 0, 0
    while i < n and j < m:
        if a_sum < b_sum:
            a_total += a[i]
            a_sum += a[i]
            i += 1
        else:
            b_total += b[j]
            b_sum += b[j]
            j += 1
        if a_sum == b_sum:
            count += 1
            a_sum, b_sum = 0, 0
    while i < n and a_total < b_total:
        a_total += a[i]
        i += 1
    while j < m and b_total < a_total:
        b_total += b[j]
        j += 1
    if i == n and j == m and a_total == b_total:
        return count
    return -1


def __starting_point():
    print(main())


__starting_point()
