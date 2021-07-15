import numpy as np
import sys
def sinput(): return sys.stdin.readline()
def iinput(): return int(sinput())
def imap(): return map(int, sinput().split())
def fmap(): return map(float, sinput().split())
def iarr(): return list(imap())
def farr(): return list(fmap())
def sarr(): return sinput().split()

s = input()
p = g = ans = 0
for i in s:
    if i=='p':
        if p < g: p += 1
        else: ans -= 1; g += 1
    if i=='g':
        if p < g: ans += 1; p += 1
        else: g += 1
print(ans)
