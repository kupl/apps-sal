import functools
import math

N, X = [int(i) for i in input().split()]
x_list = [int(i) for i in input().split()]

x_list.append(X)
num_list = sorted(x_list)
 
tmp = [abs(x[0] - x[1]) for x in zip(num_list[:-1],num_list[1:])]

D = functools.reduce(lambda acc, x: math.gcd(acc, x), tmp, 0)

print(D)

