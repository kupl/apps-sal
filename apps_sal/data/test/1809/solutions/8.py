__author__ = 'Rakshak.R.Hegde'
'\nCreated on Dec 30 2014 PM 09:40\n\n@author: Rakshak.R.Hegde\n'
from collections import deque
from bisect import bisect


def mint():
    return map(int, input().split())


(n, m) = mint()
w = tuple(mint())
b = mint()
stack = []
lifts = 0
for x in b:
    for (i, v) in enumerate(stack):
        if v == x:
            stack.pop(i)
            break
    else:
        i = 0
    for i in range(i, len(stack)):
        lifts += w[stack[i] - 1]
    stack.append(x)
print(lifts)
