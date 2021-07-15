#!/usr/bin/env python3
import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()


def per(n, r, mod=10**9+7):  # 順列数
    per = 1
    for i in range(r):
        per = per*(n-i) % mod
    return per


def com(n, r, mod=10**9+7):  # 組み合わせ数
    bunshi = per(n, r, mod)
    bunbo = 1
    for i in range(1, r+1):
        bunbo = bunbo*i % mod
    return bunshi*pow(bunbo, -1, mod) % mod


def main():
    n = list(map(int, list(input())))
    k = int(input())
    keta = len(n)
    count = [n[0]-1+com(keta-1, 1)*9, (n[0]-1)*com(keta-1, 1)*9+com(keta-1, 2)
             * 9**2, (n[0]-1)*com(keta-1, 2)*9**2+com(keta-1, 3)*9**3]
    nonzero = 1
    #print(count)
    for i in range(1, keta):
        if n[i] != 0:
            nonzero+=1
            if nonzero==2:
                count[1]+=(n[i]-1)+com(keta-i-1,1)*9
                count[2]+=(keta-i-1)*(n[i]-1)*9+com(keta-i-1,2)*9**2
            elif nonzero==3:
                count[2]+=(n[i]-1)+com(keta-i-1,1)*9
        #print(count)
    print((count[k-1]+(nonzero>=k)))



def __starting_point():
    main()

__starting_point()
