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


s = insr()

for i in range(0, len(s), 2):
    if s[i] == 'L':
        print("No")
        return

for i in range(1, len(s), 2):
    if s[i] == 'R':
        print("No")
        return

print("Yes")
