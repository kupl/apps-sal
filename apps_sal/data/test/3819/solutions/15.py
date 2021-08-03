from sys import stdin
from collections import deque

n = int(stdin.readline())

hand = [int(x) for x in stdin.readline().split()]

deck = [int(x) for x in stdin.readline().split()]

ind = {}

for i, x in enumerate(deck):
    if x != 0:
        ind[x] = i

offset = sorted([(ind[i] - i + 2, i) for i in ind])

if not offset:
    print(n)

elif not 1 in deck:
    print(max(offset[-1][0] + n, n))
else:
    i1 = deck.index(1)
    newD = deck[i1:]
    valid = True
    for x in range(len(newD) - 1):
        if newD[x] > newD[x + 1]:
            valid = False
            break
    if valid:
        v2 = True
        newOff = i1 - n
        for o, x in offset:
            if x > -newOff and o > newOff:
                v2 = False
                break

        if v2:
            print(newOff + n)
        else:
            print(max(offset[-1][0] + n, n))
    else:
        print(max(offset[-1][0] + n, n))
