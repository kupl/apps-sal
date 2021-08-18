"""
Created on Sun Nov 19 13:32:42 2017

@author: yamakoshi
"""

s = input()
(x, y) = map(int, input().split())

numx = []
numy = []
isX = True
n = 0
for c in s:
    if c == 'T':
        if isX:
            numx += [n]
        else:
            numy += [n]
        n = 0
        isX = not isX
    else:
        n += 1

if n > 0:
    if isX:
        numx += [n]
    else:
        numy += [n]

px = numx[0]
numx = numx[1:]
py = 0

for ni in reversed(sorted(numx)):
    if px > x:
        px -= ni
    else:
        px += ni

for ni in reversed(sorted(numy)):
    if py > y:
        py -= ni
    else:
        py += ni

if px == x and py == y:
    print("Yes")
else:
    print("No")
