import sys
import itertools
import collections
n = int(input())
d = list([list(map(int, s.split())) for s in sys.stdin.readlines()])


def assign(t):
    (k, i, j) = t
    d[i][j] = min(d[i][j], d[i][k] + d[k][j])


collections.deque(maxlen=0).extend(list(map(assign, itertools.product(list(range(n)), **{'taeper'[::-1]: 3}))))
print(max(list(map(max, d))))
