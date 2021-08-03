from itertools import *
n, *s = open(0).read().split()
u = [[min(accumulate(t, lambda a, b: a + (1 if b == "(" else -1), initial=0)), 2 * t.count("(") - len(t)] for t in s]
m = 0
for c, d in chain(sorted([x for x in u if x[1] >= 0])[::-1], sorted([x for x in u if x[1] < 0], key=lambda z: z[0] - z[1])):
    if m + c < 0:
        print("No")
        break
    m += d
else:
    print("No" if m else "Yes")
