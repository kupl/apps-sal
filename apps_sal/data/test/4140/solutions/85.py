#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline
import numpy as np

def main():
    S = np.array(list(map(int,input().rstrip())))
    L = len(S)
    A = np.arange(L) & 1
    B = 1 - A
    x1 = (A!=S).sum()
    x2 = (B!=S).sum()
    print(min(x1,x2))

def __starting_point():
    main()
__starting_point()
