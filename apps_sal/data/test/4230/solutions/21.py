#                               #
# author : samars_diary #
# 18-09-2020 │ 19:20:45 #
#                               #

import sys
import os.path

# if(os.path.exists('input.txt')):
#sys.stdin = open('input.txt',"r")
#sys.stdout = open('output.txt',"w")

sys.setrecursionlimit(10 ** 5)


def mod(): return 10**9 + 7
def i(): return sys.stdin.readline().strip()
def ii(): return int(sys.stdin.readline())
def li(): return list(sys.stdin.readline().strip())
def mii(): return map(int, sys.stdin.readline().split())
def lii(): return list(map(int, sys.stdin.readline().strip().split()))

# print=sys.stdout.write


def solve():
    a, b = mii()
    if b == 0:
        print(a)
        return
    c = lii()
    d = 111
    e = 0
    for i in range(max(c) + 2):
        if i not in c:
            if abs(i - a) < d:
                d = abs(i - a)
                e = i
    print(e)


for _ in range(1):
    solve()
