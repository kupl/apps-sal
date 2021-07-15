from collections import defaultdict as dd, deque
n = int(input())
A = [int(x) for x in input().split()]
n = len(A)

C = dd(int)
for a in A:
    C[a] += 1

thedup = None
ndup = 0
screwed = False
for c in C:
    if C[c] > 2:
        screwed = True
    elif C[c] == 2:
        if c == 0:
            screwed = True
        thedup = c
        ndup += 1

import sys
if screwed or ndup > 1:
    print('cslnb')
else:
    if ndup == 1:
        if C[thedup-1] != 0:
            print('cslnb')
            return
        

    target = sum(range(n))
    cur = sum(A)
    togo = cur - target

    if togo%2 == 0:
        print('cslnb')
    else:
        print('sjfnb')

