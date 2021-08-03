from functools import reduce
import math
N = int(input())
T = [int(input()) for _ in range(N)]


print(reduce(lambda x, y: (x * y) // math.gcd(x, y), T, 1))
