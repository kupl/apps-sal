from functools import reduce
import math
_ = input()
a = sorted(set(map(int, input().split())))
print(reduce(math.gcd, a))
