import numpy as np
from functools import reduce
_ = input()
print(reduce(np.gcd, map(int, input().split())))
