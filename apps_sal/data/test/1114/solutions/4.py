__author__ = 'MoonBall'

import sys
# sys.stdin = open('data/B.in', 'r')
T = 1

def process():
    N, M = list(map(int, input().split()))
    f = list(map(int, input().split()))
    b = list(map(int, input().split()))

    fc = {}
    for idx, fv in enumerate(f): fc[fv] = (1, idx) if not fc.get(fv) else (fc[fv][0] + 1, idx)

    a = []
    failed = False
    multi = False
    for bv in b:
        if not fc.get(bv):
            failed = True
            continue
        if fc[bv][0] > 1:
            multi = True
            continue
        a.append(fc[bv][1] + 1)

    if failed:
        print('Impossible')
    elif multi:
        print('Ambiguity')
    else:
        print('Possible')
        print(' '.join(map(str, a)))







for _ in range(T):
    process()

