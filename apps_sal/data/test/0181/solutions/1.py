from functools import reduce
from math import factorial
n = (int(input()) + 45) % 360
print(n // 90 - (n > 0 and n%90 == 0))


