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


n, k, p = invr()
a = inara()
b = inara()
a.sort()
b.sort()

ans = int(1e18)
for i in range(k - n + 1):
    curr = -1
    for j in range(n):
        if p <= b[i + j] and b[i + j] <= a[j]:
            curr = max(curr, a[j] - p)
        elif a[j] <= b[i + j] and b[i + j] <= p:
            curr = max(curr, p - a[j])
        else:
            curr = max(curr, abs(a[j] - b[i + j]) + abs(p - b[i + j]))
    ans = min(ans, curr)
print(ans)
