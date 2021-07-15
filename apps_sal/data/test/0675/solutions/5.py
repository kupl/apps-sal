import math
import sys

debug = False

if debug:
    fin = open('input.txt', 'r')
    fout = open('output.txt', 'w')
else:
    fin = sys.stdin
    fout = sys.stdout

s = fin.readline()
m, t, r = list(map(int, s.split()))

if r > t:
    fout.write('-1')
    return

s = fin.readline()
w = list(map(int, s.split()))

ans = r
ar = [w[0] - r + i for i in range(r)]
for i in range(1, m):
    while ar and w[i] - ar[0] > t:
        ar.pop(0)
    ans += r - len(ar)
    b = r - len(ar)
    for j in range(b):
        ar.append(w[i] - b + j)

fout.write(str(ans))

