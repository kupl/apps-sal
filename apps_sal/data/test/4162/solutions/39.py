#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline
import numpy as np

def main():
    numbers=[]
    n = int(input())
    numbers=np.array(list(map(int,input().split())))

    print((numbers-1).sum())

    

def __starting_point():
    main()
__starting_point()
