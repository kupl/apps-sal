# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 15:41:54 2016

@author: kebl4230

Too slow. Possibly lots of unnecessary list manipulation.
"""
from functools import cmp_to_key
n = int(input())
strings = list()
for i in range(n):
    strings.append(input())


def cmpfunc(x, y):
    a = x + y
    b = y + x
    if a < b:
        return -1
    elif a == b:
        return 0
    else:
        return 1


bb = sorted(strings, key=cmp_to_key(cmpfunc))
print("".join(bb))


"""
n = int(input())
strings = list()
for i in range(n):
    strings.append(input())

aa = "abcdefghijklmnopqrstuvwxyz"
positions = [strings.copy()]


def myfunc(mylist, index, pos):
    scores = [aa.find(bb[index]) if index < len(bb) else 27 for bb in mylist]
    r = 0
    mins = min(scores)
    while mins <= 27:
        if r == 0:
            for i in range(len(scores)):
                if scores[i] == mins:
                    scores[i] = 100
        else:
            group = [mylist[n] for n in range(len(scores)) if scores[n] == mins]
            positions.insert(pos + r, group)
            for string in group:
                mylist.remove(string)
            while any(s == mins for s in scores):
                scores.remove(mins)
        r += 1
        mins = min(scores)

index = 0
maxlen = len(positions)
pos = 0
while any(len(pos) > 1 for pos in positions):
    myfunc(positions[pos], index, pos)
    pos += 1
    if pos == maxlen:
        pos = 0
        maxlen = len(positions)
        index += 1

result = ''
for aa in positions:
    result += aa[0]
print(result)
"""
