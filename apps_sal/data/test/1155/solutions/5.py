import random
import functools
import itertools
import math
R = lambda type_='int': list(map(eval(type_), input().split(' ')))
(n, m) = R()
ans = 10000000000000
for i in range(n):
    (a, b) = R()
    ans = min(ans, a / b)
print(ans * m)
