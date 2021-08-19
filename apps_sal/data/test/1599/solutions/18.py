import sys
import math
st = sys.stdin.readline()
length = len(st) - 1
an = [0] * length
v = st[0]
for i in range(1, length):
    k = 0
    if v == st[i]:
        k = 1
    v = st[i]
    an[i] = an[i - 1] + k
c = int(sys.stdin.readline())
for i in range(c):
    (li, ri) = [int(x) for x in sys.stdin.readline().split()]
    print(an[ri - 1] - an[li - 1])
