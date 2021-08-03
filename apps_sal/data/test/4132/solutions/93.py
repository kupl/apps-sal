from functools import reduce
import math
N = int(input())
A = map(int, input().split())

print(reduce(math.gcd, A))
