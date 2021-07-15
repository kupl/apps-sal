import math
import sys
import getpass
import bisect


def ria():
    return [int(i) for i in input().split()]


files = True

if getpass.getuser().lower() == 'frohe' and files:
    sys.stdin = open('test.in')
    # sys.stdout = open('test.out', 'w')

n = ria()[0]
nm = {}
for i in range(n):
    ar = [i.strip() for i in input().split()]
    name = ar[0]
    if not (name in nm):
        nm[name] = []
    for j in ar[2:]:
        nm[name].append(j)
for i in nm:
    nm[i] = sorted(nm[i], key=lambda x: len(x))

nmfin = {}
for i in nm:
    cur = nm[i]
    nmfin[i] = []
    for j in range(len(cur)):
        bad = False
        for j1 in range(j + 1, len(cur)):
            if cur[j1].endswith(cur[j]):
                bad = True

                break
        if not bad:
            nmfin[i].append(cur[j])
print(len(nmfin))
for i in nmfin:
    print(i,len(nmfin[i]), end=' ')
    for j in nmfin[i]:
        print(j,end=' ')
    print()

