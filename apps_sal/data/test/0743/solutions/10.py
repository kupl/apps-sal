from functools import *; from fractions import*
print(int(input()) * reduce(gcd,list(map(int,input().split()))))


