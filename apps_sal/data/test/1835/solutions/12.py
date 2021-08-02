import sys
from collections import deque
readline = sys.stdin.readline
q = int(readline())

for _ in range(q):
    n = int(readline())
    tmp = []
    ans = False
    c = 0
    for i in range(n):
        s = str(readline().split()[0])
        tmp.append(s)
        if len(s) % 2 == 1:
            ans = True
        for ss in s:
            if ss == '1':
                c += 1
    if ans or c % 2 == 0:
        print(n)
    else:
        print(n - 1)
