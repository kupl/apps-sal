import itertools

def f(x):
    scores = [0, 0]
    for i in itertools.cycle([0, 1]):

        if x & 1:
            scores[i] += 1
            x -= 1

        elif x == 0:
            return scores[0]

        elif x == 4 or x & 0b10:
            x >>= 1
            scores[i] += x
        else:
            x -= 1
            scores[i] += 1


N = int(input())
results = []

import sys
for n in map(f, map(int, sys.stdin.read().split())):
    results.append(n)

print('\n'.join(map(str, results)))
