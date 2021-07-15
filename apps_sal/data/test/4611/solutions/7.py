#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

n = int(input())

t, x, y = 0, 0, 0
for i in range(n):
    t_new, x_new, y_new = list(map(int, input().split()))

    time = t_new-t
    dis = abs(x_new-x)+abs(y_new-y)

    if time < dis:
        print("No")
        return
    if time % 2 != dis % 2:
        print("No")
        return
    t, x, y = t_new, x_new, y_new
print("Yes")

