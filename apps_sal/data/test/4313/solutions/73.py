# coding: UTF-8
import sys
import numpy as np


n = int(input())
vList = list(map(int, input().split()))
cList = list(map(int, input().split()))
ans = 0
for v, c in zip(vList, cList):
    ans += max(v - c, 0)
print(ans)
