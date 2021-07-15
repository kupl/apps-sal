#!/usr/bin/env python3
# -*- coding: utf-8 -*-

k = int(input())
str = input()

dic = {}
for i in str:
    if i not in dic:
        dic[i]  = 1
    else:
        dic[i] += 1

if ( k > len(dic)):
    print("NO")
else:
    print("YES", end='')
    dic2 = []
    n = 0

    for i in str:
        if (i not in dic2) and n < k:
            print()
            print(i, end='')
            n += 1
            dic2.append(i)
        else:
            print(i, end='')

    print()


