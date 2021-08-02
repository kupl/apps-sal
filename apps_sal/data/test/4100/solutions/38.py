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


n, k, q = invr()

ara = [k] * n

for i in range(q):
    x = inp()
    x -= 1
    ara[x] += 1

for i in range(n):
    if ara[i] - q > 0:
        print("Yes")
    else:
        print("No")
