# Referred to https://atcoder.jp/contests/abc158/submissions/17106264
from collections import deque
s, j = deque(input()), False
for _ in range(int(input())):
    t = input().split()
    if t[0] == '1':
        j = not j
        continue
    if t[1] == '1':
        if j:
            s.append(t[2])
        else:
            s.appendleft(t[2])
    else:
        if j:
            s.appendleft(t[2])
        else:
            s.append(t[2])
if j:
    s.reverse()
print(*s, sep='')
