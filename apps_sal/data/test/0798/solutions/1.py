from fractions import *
import sys
def check(a):
    if a % 2 != 0:
        return False
    if a<0:
        return False
    return True
readln = lambda:map(int,input().split())
a,b,c = readln()
if not check(b+c-a) or not check(a+b-c) or not check(a+c-b):
    print("Impossible")
    return
s23 = (b+c-a)//2
s12 = (a+b-c)//2
s13 = (a+c-b) //2
print(s12,s23,s13)
