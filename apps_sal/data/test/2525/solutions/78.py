import math
import collections
from itertools import product


def ii():
    return int(input())


def mi():
    return map(int, input().split())


def li():
    return list(map(int, input().split()))


s = input()
q = ii()
query = [input().split() for _ in range(q)]
front = []
back = []
cnt1 = 0
for i in range(q):
    if query[i][0] == '1':
        cnt1 += 1
    elif cnt1 % 2 == 0:
        if query[i][1] == '1':
            front.append(query[i][2])
        else:
            back.append(query[i][2])
    elif query[i][1] == '1':
        back.append(query[i][2])
    else:
        front.append(query[i][2])
if cnt1 % 2 == 0:
    print(''.join(front[::-1]) + s + ''.join(back))
else:
    print(''.join(back[::-1]) + s[::-1] + ''.join(front))
