import math, sys
from fractions import *

def mp():
    return list(map(int, input().split()))

def f(q):
    if q == -1:
        return 0
    return -1

def main():
    a = input().strip()
    if len(a) % 2 == 0:
        q = -1
    else:
        q = 0
    ans = ''
    while len(a):
        ans = a[q] + ans
        if q == -1:
            a = a[:len(a) - 1]
        else:
            a = a[1:]
        q = f(q)
    print(ans)
        
deb = 0
if deb:
    file = open('input.txt', 'w')
else:
    input = sys.stdin.readline
    
main()
