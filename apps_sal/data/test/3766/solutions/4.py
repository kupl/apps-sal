from itertools import *
def power(i): return chain.from_iterable(combinations(i, r) for r in range(len(i) + 1))


input()
cards = set(input().split())
print((min(len(s) for s in power("RGBYW12345") if
           len(set(str(set(s) & set(t)) for t in cards)) == len(cards)
           )))
