from collections import defaultdict
from functools import reduce


def mi(): return [int(i) for i in input().split()]
def flat(l): return reduce(lambda a, b: a + b, l)


t = mi()[0]

for _ in range(t):
    n = mi()[0]
    s = input()

    # print(min(s.find('>'), (len(s) - s.rfind('<') - 1)))
    print(min(len(s) - len(s.lstrip('<')), len(s) - len(s.rstrip('>'))))
