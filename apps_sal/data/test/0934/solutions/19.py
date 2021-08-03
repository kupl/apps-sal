import re
import math
import decimal
import bisect
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]


# code goes here
card = read()
mine = read().split()
for c in mine:
    if c[0] == card[0] or c[1] == card[1]:
        print("YES")
        return

print("NO")
