import sys
import itertools
tokens = itertools.chain.from_iterable(list(map(str.split, sys.stdin)))
no = 'IMPOSSIBLE'
a = int(next(tokens))
b = int(next(tokens))
k = (a ** 2 - b ** 2) // (2 * (a - b))
if abs(a - k) != abs(b - k):
    print(no)
else:
    print(k)
