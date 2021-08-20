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
print(''.join(bb))
'\nn = int(input())\nstrings = list()\nfor i in range(n):\n    strings.append(input())\n\naa = "abcdefghijklmnopqrstuvwxyz"\npositions = [strings.copy()]\n\n\ndef myfunc(mylist, index, pos):\n    scores = [aa.find(bb[index]) if index < len(bb) else 27 for bb in mylist]\n    r = 0\n    mins = min(scores)\n    while mins <= 27:\n        if r == 0:\n            for i in range(len(scores)):\n                if scores[i] == mins:\n                    scores[i] = 100\n        else:\n            group = [mylist[n] for n in range(len(scores)) if scores[n] == mins]\n            positions.insert(pos + r, group)\n            for string in group:\n                mylist.remove(string)\n            while any(s == mins for s in scores):\n                scores.remove(mins)\n        r += 1\n        mins = min(scores)\n\nindex = 0\nmaxlen = len(positions)\npos = 0\nwhile any(len(pos) > 1 for pos in positions):\n    myfunc(positions[pos], index, pos)\n    pos += 1\n    if pos == maxlen:\n        pos = 0\n        maxlen = len(positions)\n        index += 1\n\nresult = \'\'\nfor aa in positions:\n    result += aa[0]\nprint(result)\n'
