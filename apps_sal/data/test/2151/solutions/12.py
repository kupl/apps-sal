import re
import math
import decimal
import bisect
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]


# code goes here
for q in range(iread()):
    n = iread()
    seq = read()
    a = int(seq[0])
    b = int(seq[1:])
    if a < b:
        print("YES")
        print(2)
        print(a, b)
    else:
        print("NO")
