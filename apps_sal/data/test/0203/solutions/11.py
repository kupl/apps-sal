from collections import deque

n = int(input())
s = input()

d = deque()
r = deque()

for i, c in enumerate(s):
    if c == 'D':
        d.append(i)
    else:
        r.append(i)

while len(d) > 0 and len(r) > 0:
    if d[0] < r[0]:
        d.append(d.popleft() + n)
        r.popleft()
    else:
        d.popleft()
        r.append(r.popleft() + n)

print('D' if len(d) > 0 else 'R')
