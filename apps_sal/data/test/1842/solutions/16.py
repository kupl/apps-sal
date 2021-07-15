from math import *

a, b, c = [int(t) for t in input().split()]
d = b*b - 4*a*c

l = (-b+sqrt(d))/(2*a)
r = (-b-sqrt(d))/(2*a)

print(max(l, r), min(l, r), sep='\n')
