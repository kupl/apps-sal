from math import*

A,B,H,M = map(int, input().split())

print((A*A+B*B-2*A*B*cos((M*11/360-H/6)*pi))**.5)
