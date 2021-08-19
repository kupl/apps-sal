import sys
import math
#from queue import *
#import random
# sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

############ ---- USER DEFINED INPUT FUNCTIONS ---- ############


def inp():
    return(int(input()))


def inara():
    return(list(map(int, input().split())))


def insr():
    s = input()
    return(list(s[:len(s) - 1]))


def invr():
    return(list(map(int, input().split())))
################################################################
############ ---- THE ACTUAL CODE STARTS BELOW ---- ############


t = inp()

for _ in range(t):
    l, r = invr()

    if l * 2 > r:
        print(-1, -1)
    else:
        print(l, 2 * l)
