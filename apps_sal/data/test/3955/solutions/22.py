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


n, k, x = invr()
ara = inara()
ara.append(0)
ara.reverse()
ara.append(0)
ara.reverse()

mul = int(math.pow(x, k))

pref = [0] * (n + 2)

for i in range(1, n + 1):
    pref[i] = pref[i - 1] | ara[i]

suff = [0] * (n + 2)

for i in range(n, 0, -1):
    suff[i] = suff[i + 1] | ara[i]

ans = 0

for i in range(1, n + 1):
    ans = max(ans, pref[i - 1] | ara[i] * mul | suff[i + 1])

print(ans)
