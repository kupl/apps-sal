import sys;
import math
import time
import random
import functools

def pal(x):
    for i in range(len(x)//2):
        if x[i] != x[len(x) - i - 1]:
            return False
    return True

s = input()
k = int(input())

l = 0
if len(s)%k == 0:
    l = len(s)//k
else:
    print("NO")
    return

for i in range(k):
    q = ""
    for j in range(l*i, l*i+l):
        q+=s[j]
    if not pal(q):
        print("NO")
        return

print("YES")
