# -*- coding: utf-8 -*-

N = int(input())
A = int(input())

remainder = N % 500
if A > remainder or remainder==0:
    print("Yes")
else:
    print("No")
