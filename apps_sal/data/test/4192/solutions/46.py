import sys

d, t, s = sys.stdin.readline().strip().split(' ')
d = int(d)
t = int(t)
s = int(s)
if d <= t * s:
    print('Yes')
else:
    print('No')
