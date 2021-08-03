import sys
import itertools
tokens = itertools.chain.from_iterable(list(map(str.split, sys.stdin)))

yesno = ['NO', 'YES']
n = int(next(tokens))
p = [int(next(tokens)) for _ in range(n)]


s = sum(1 if a != b else 0 for a, b in zip(p, sorted(p)))
print((yesno[s == 2 or s == 0]))
