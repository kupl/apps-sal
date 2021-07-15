from math import gcd as g

a, b, c, d = map(int,input().split())
count = 0

print(b - a + 1 - (b // c - (a-1) // c + b // d - (a-1) // d - b // ((c*d)//g(c,d)) + (a-1) // ((c*d)//g(c,d))))
