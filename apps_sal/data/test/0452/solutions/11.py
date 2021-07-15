#!/usr/bin/env python
#coding:utf-8

from fractions import Fraction

def frac(lis,i):
    if i == len(lis)-1 :
        return lis[i]
    else:
        return lis[i]+1/frac(lis,i+1)

def main():
    linesp = input().split(" ")
    p,q = int(linesp[0]),int(linesp[1])
    one = Fraction(p,q)

    n = int(input())

    A = []
    for s in input().split(" "):
        A.append(Fraction(int(s)))

    two = frac(A,0)
    if one == two:
        print("YES")
    else:
        print("NO")

def __starting_point():
    main()

__starting_point()
