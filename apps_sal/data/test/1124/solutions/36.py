import functools
import math
n = int(input())
a = list(map(int, input().split()))
a = list(set(a))
ans = 0
x = functools.reduce(math.gcd, a)
print(x)

