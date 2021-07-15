import functools
import math

N, X = [int(i) for i in input().split()]
x_list = [abs(int(i) - X) for i in input().split()]

D = functools.reduce(lambda acc, x: math.gcd(acc, x), x_list, 0)

print(D)
