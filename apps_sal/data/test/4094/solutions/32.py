#                               #
    # author : samars_diary #
    # 17-09-2020 │ 16:21:14 #
#                               #

import sys, os.path

#if(os.path.exists('input.txt')):
    #sys.stdin = open('input.txt',"r")
    #sys.stdout = open('output.txt',"w")

sys.setrecursionlimit(10 ** 5)

def mod(): return 10**9+7
def i(): return sys.stdin.readline().strip()
def ii(): return int(sys.stdin.readline())
def li(): return list(sys.stdin.readline().strip())
def mii(): return map(int, sys.stdin.readline().split())
def lii(): return list(map(int, sys.stdin.readline().strip().split()))

#print=sys.stdout.write

def solve():
    a=ii()
    val=7%a
    for i in range(1,10**7):
        if val==0:
            print(i)
            return
        val=(val*10+7)%a
    print(-1)
for _ in range(1):
    solve()
