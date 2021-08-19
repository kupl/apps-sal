import sys
sin = sys.stdin
sin.readline()
arr = sin.readline().split()
arr = [int(i) for i in arr]
lp = ln = ep = en = 0
for i in arr:
    newNeg = 0
    newPos = 0
    if i < 0:
        newNeg = ep + 1
        newPos = en
    if i > 0:
        newNeg = en
        newPos = ep + 1
    lp += ep
    ln += en
    ep = newPos
    en = newNeg
print(ln + en, lp + ep)
