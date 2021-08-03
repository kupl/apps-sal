import math
import functools

N, X = list(map(int, input().split()))
A = [abs(X - int(i)) for i in input().split()]

print((functools.reduce(math.gcd, A)))
