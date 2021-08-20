import itertools
import math
s = input().split()
n = int(s[0])
i = s[2] == 'week'
if i:
    print(366 // 7 + (5 <= n <= 6))
elif n <= 29:
    print(12)
elif n == 30:
    print(11)
else:
    print(7)
