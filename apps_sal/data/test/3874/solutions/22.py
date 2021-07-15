"""
Oh, Grantors of Dark Disgrace, 
Do Not Wake Me Again.
"""

import sys

ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
si = lambda: input()

n, m = mi()
f = []

for i in range(n):
    f.append(si())

lm = li()

l = len(f[lm[0]-1])
z = ['']*l

for v in lm:
    if len(f[v-1]) != l:
        print("No")
        return
    else:
        for i in range(len(z)):
            z[i] += f[v-1][i]

x = ''

for i in range(len(z)):
    if len(set(z[i])) == 1:
        x += z[i][0]
    else:
        x += '?'

for i, j in enumerate(f):
    if i+1 in lm or len(j) != l: continue
    else:
        b = 1
        for p in range(len(j)):
            if x[p]!='?' and (x[p] != j[p]):
                b = 0
        if b == 1:
            print("No")
            return

print("Yes")
print(x)
