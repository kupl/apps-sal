import math
import sys
n = int(input())
dicn = [{} for i in range(10 ** 6)]
maxv = set()
v = {'a', 'e', 'i', 'o', 'u'}
for i in range(n):
    t = input()
    c = 0
    lv = ''
    for l in t:
        if l in v:
            c += 1
            lv = l
    if lv in dicn[c - 1]:
        dicn[c - 1][lv].append(t)
    else:
        dicn[c - 1][lv] = [t]
    maxv.add(c)
maxv = sorted(list(maxv))
first = [[] for i in range(maxv[-1])]
second = []
for i in maxv:
    for j in dicn[i - 1]:
        if len(dicn[i - 1][j]) % 2 == 1:
            first[i - 1].append(dicn[i - 1][j].pop())
        if len(dicn[i - 1][j]) > 0:
            second += dicn[i - 1][j]
t = []
c = 0
for f in first:
    while len(f) >= 2 and len(second) >= 2:
        c += 1
        t.append(' '.join([f.pop(), second.pop()]))
        t.append(' '.join([f.pop(), second.pop()]))
while len(second) >= 4:
    c += 1
    q = []
    w = []
    q.append(second.pop())
    w.append(second.pop())
    q.append(second.pop())
    w.append(second.pop())
    t.append(' '.join(q))
    t.append(' '.join(w))
print(len(t) // 2)
for i in t:
    print(i)
