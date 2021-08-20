from functools import reduce
import math
(N, X) = map(int, input().split())
(*C,) = map(int, input().split())
t = [abs(c - X) for c in C]
print(reduce(math.gcd, t))
