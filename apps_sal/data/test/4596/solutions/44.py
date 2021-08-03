#!/usr/bin/env python3
import math
import sys
sys.setrecursionlimit(10**6)


n = int(input())
a = list(map(int, input().split()))

ans = 10**10

for i in a:
    tmp = 0
    while(i % 2 != 1):
        tmp += 1
        i = i // 2
    # print(tmp)
    ans = min(ans, tmp)

print(ans)
