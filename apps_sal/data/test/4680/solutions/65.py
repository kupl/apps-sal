#!/usr/bin/env python3
# -*- coding: utf-8 -*-

a = list(map(int, input().split()))

if 7 == a[0]:
    if 5 == a[1] and 5 == a[2]:
        print("YES", end="\n")
    else:
        print("NO", end="\n")   

elif 5 == a[0]:
    if (7 == a[1] and 5 == a[2]) or (5 == a[1] and 7 == a[2]):
        print("YES", end="\n")
    else:
        print("NO", end="\n")   
else:
    print("NO", end="\n")
