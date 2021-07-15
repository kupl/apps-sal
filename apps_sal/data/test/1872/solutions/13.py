from sys import stdin
from math import pi, sin, tan
n, r = map(int, stdin.readline().split())
a = 2*pi/n
A = r*r/2 * (a - sin(a))
c = n//2 * 2*pi/n
b = (c-a)/2
s = 2*r*sin(a/2)
h = tan(b)*s/2
A = A + h*s/2
result = pi*r*r - n*A
print(result)
