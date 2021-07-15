import os, sys

n = int(input())
text = sys.stdin.readline()
a = list(sorted(map(int, text.strip().split())))

m = 150002
lsg = []
while a:
    n = a.pop()
    if n+1 < m:
        m = n+1
        lsg.append(m)
    elif n < m:
        m = n
        lsg.append(m)
    elif n-1 < m:
        m = n-1
        lsg.append(m)

l = len(lsg)
print(l-1 if lsg[-1] == 0 else l)

