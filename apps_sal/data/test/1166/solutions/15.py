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
    bs = set()
    moves = {}
    for i in range(n):
        moves[a[i]] = list(a[j] for j in range(i % a[i], n, a[i]) if a[j] > a[i])
    winners = {}
    for i in range(n, 0, -1):
        winner = 'A' if any(winners[j] == 'B' for j in moves[i]) else 'B'
        if winner == 'B':
            bs.add(i)
        winners[i] = winner
    print(''.join(winners[ai] for ai in a))


def __starting_point():
    main()


__starting_point()
