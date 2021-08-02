from sys import *
from math import *
from collections import *

N = int(input())

S = input()


e = deque([])
n = deque([])

for i, v in enumerate(S):
    if v == '8':
        e += [i]
    else:
        n += [i]

todo = (N - 11) // 2

for i in range(todo):
    if len(n) != 0:
        n.popleft()
    else:
        e.pop()

    if len(e) != 0:
        e.popleft()
    else:
        n.pop()

if len(e) != 0 and (len(n) == 0 or n[0] > e[0]):
    print("YES")
else:
    print("NO")
