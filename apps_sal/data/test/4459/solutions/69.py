#!/usr/bin/env python3

# import
#import math
#import numpy as np
N = int(input())
# = input()
# = map(int, input().split())
A = list(map(int, input().split()))
# = [input(), input()]
# = [list(map(int, input().split())) for _ in range(N)]
# = [int(input()) for _ in range(N)]
# = {i:[] for i in range(N)}

dic = {}

for a in A:
    if a in dic:
        dic[a] += 1
    else:
        dic[a] = 1

ans = 0

for key in dic:
    if dic[key] != key:
        if dic[key] > key:
            ans += dic[key] - key
        else:
            ans += dic[key]

print(ans)
