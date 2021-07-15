import bisect
import sys
import math
input = sys.stdin.readline
import functools

from collections import defaultdict

############ ---- Input Functions ---- ############

def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(list(map(int,input().split())))

############ ---- Solution ---- ############

def solve(case):
    [x, y, n] = inlt()
    res = (n // x) * x + y
    if res > n:
        res -= x
    return res
    

if len(sys.argv) > 1 and sys.argv[1].startswith("input"):
    f = open("./" + sys.argv[1], 'r')
    input = f.readline

T = inp()
for i in range(T):
    res = solve(i+1)
    print(str(res))

