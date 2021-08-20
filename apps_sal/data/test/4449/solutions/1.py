from sys import stdin
from collections import deque
q = int(stdin.readline().strip())
for i in range(q):
    n = int(stdin.readline().strip())
    s = list(map(int, stdin.readline().strip().split()))
    s.sort()
    s = deque(s)
    t = True
    A = s[0] * s[-1]
    while len(s) > 0:
        a1 = s[0] * s[-1]
        if a1 != A or s[0] != s[1] or s[-1] != s[-2]:
            t = False
            break
        s.popleft()
        s.popleft()
        s.pop()
        s.pop()
    if t:
        print('YES')
    else:
        print('NO')
