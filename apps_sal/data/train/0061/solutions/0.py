import sys
import math
#from queue import *
import random
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
    n = inp()
    ara = inara()

    ans = []

    for i in range(1, n - 1):
        if ara[i] > ara[i - 1] and ara[i] > ara[i + 1]:
            ans.append(i)
            ans.append(i + 1)
            ans.append(i + 2)
            break

    if len(ans) == 0:
        print("NO")
    else:
        print("YES")
        print(*ans)
