import sys
import copy
import math
import itertools
import numpy as np

l = [int(c) for c in input().split()]
A=l[0]
B=l[1]
S=input()

if S[A] == "-" and str.isdecimal(S[0:A]+S[A+1:A+B]):
    print("Yes")
else:
    print("No")
