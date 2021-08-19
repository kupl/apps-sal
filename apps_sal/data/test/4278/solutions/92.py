import collections
import math
n = int(input())
s = [input() for i in range(n)]
for i in range(n):
    s[i] = list(s[i])
    s[i].sort()
    s[i] = ''.join(s[i])
c = collections.Counter(s)
a = 0
for i in c.values():
    if i > 1:
        a += i * (i - 1) // 2
print(a)
