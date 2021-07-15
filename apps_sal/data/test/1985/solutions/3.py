import sys

K, N = [int(x) for x in sys.stdin.readline().split()]
a_s = [int(x) for x in sys.stdin.readline().split()]
b_s = [int(x) for x in sys.stdin.readline().split()]

poss = set([])
start = 1
for b in b_s:
    locls = set([])
    for a in a_s:
        b -= a
        locls.add(b)
    if start == 1:
        poss = locls
        start = 0
    else:
        poss = set.intersection(poss, locls)

print(len(poss))

