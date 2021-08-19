import sys
import math
st = sys.stdin.readline()
d = [0] * 2
for i in st:
    if i != '\n':
        d[ord(i) - 120] += 1
if d[0] - d[1] > 0:
    t = ['x'] * (d[0] - d[1])
    print(''.join(t))
elif d[1] - d[0] > 0:
    t = ['y'] * (d[1] - d[0])
    print(''.join(t))
