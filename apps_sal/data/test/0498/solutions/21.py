import math
import sys

fin = sys.stdin
fout = sys.stdout
n, m, x = list(map(int, fin.readline().split()))
r = math.ceil(x / (m * 2))
d = math.ceil((x - ((r - 1) * (m * 2))) / 2)
s = ''
if x % 2 == 1:
    s = 'L'
else:
    s = 'R'
fout.write(str(r) + ' ' + str(d) + ' ' + str(s))
