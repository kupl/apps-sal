N=int(input())
T=[int(input()) for _ in range(N)]

import math
from functools import reduce

print(reduce(lambda x,y : (x * y) // math.gcd(x, y), T,1))
