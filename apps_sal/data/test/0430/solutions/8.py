from sys import stdin as cin
from itertools import product
from bisect import bisect_left as bl
from collections import Counter
n = int(cin.readline())
a = list(list(map(int, cin.readline().split())))
c = Counter(a)
if c[100] % 2 == 0 and c[200] % 2 == 0 or (c[200] % 2 != 0 and (c[100] % 2 == 0 and c[100] > 1)):
    print('YES')
else:
    print('NO')
