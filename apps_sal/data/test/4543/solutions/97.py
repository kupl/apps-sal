from math import sqrt
(a, b) = input().split()
c = a + b
if sqrt(int(c)) == int(sqrt(int(c))):
    print('Yes')
else:
    print('No')
