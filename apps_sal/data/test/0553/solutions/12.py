import operator
import itertools
n = int(input())
strings = [input() for i in range(n)]
if n == 1:
    print(6)
else:
    minDiff = 6
    for a, b in itertools.combinations(strings, 2):
        minDiff = min(minDiff, list(map(operator.eq, a, b)).count(False))
    print(int((minDiff - 1) / 2))
