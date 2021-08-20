from math import sqrt
(s, p) = input().split()
s = int(s)
p = int(p)
a = int(sqrt(s * s - 4 * p))
if a * a != s * s - 4 * p:
    print('No')
elif (a + s) % 2 != 0:
    print('No')
else:
    print('Yes')
