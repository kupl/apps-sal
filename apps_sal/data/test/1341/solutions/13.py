import sys
import math
s = sys.stdin.readline()
t = sys.stdin.readline()
sl = len(s) - 1
tl = len(t) - 1
j = 0
res = 1
for i in range(tl):
    if s[j] == t[i]:
        res += 1
        j += 1
print(res)
