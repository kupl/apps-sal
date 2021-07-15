#!/usr/bin/env python
#def input(f=open('in3')): return f.readline().rstrip()

n, m = list(map(int, input().split()))
txt = [ input() for _ in range(n) ]
sol = 0

pof = list(range(n-1))
for i in range(m):

    cli = [ rw[i] for rw in txt ]
    of = [x for (x,y) in zip(pof, [i+1 for i in pof])
            if cli[x] > cli[y]]
    if (len(of) > 0):
        sol += 1
        continue

    nf = [x for (x,y) in zip(pof, [i+1 for i in pof])
            if cli[x] < cli[y]]
    pof = [t for t in pof
             if t not in nf]

print(sol)

