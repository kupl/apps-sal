#!/usr/bin/env python3

#import
#import math
#import numpy as np
#= int(input())
S = list(input())
T = list(input())

ls = len(S); lt = len(T)

for i in range(ls - lt, -1, -1):
    isok = True
    for j in range(lt):
        if S[i + j] == "?":
            continue
        if S[i + j] != T[j]:
            isok = False
            break
    if isok:
        S[i:i+lt] = T
        ans = ""
        for s in S:
            if s == "?":
                ans += "a"
            else:
                ans += s
        print(ans)
        return

print("UNRESTORABLE")

