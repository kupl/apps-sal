import math
import sys
debug = False
if debug:
    fin = open('input.txt', 'r')
    fout = open('output.txt', 'w')
else:
    fin = sys.stdin
    fout = sys.stdout
s = fin.readline()[:-1]
a = '-1'
n = len(s)
j = -1
for i in range(len(s)):
    if int(s[i]) % 2 == 0:
        if j == -1:
            j = i
        elif s[j] > s[-1]:
            j = i
if j > -1:
    a = s[0:j] + s[-1] + s[j + 1:-1] + s[j]
fout.write(a)
