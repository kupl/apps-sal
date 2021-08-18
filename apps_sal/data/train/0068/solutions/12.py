import io
import os
import sys
import math
import heapq

input = sys.stdin.readline
mod = 10**9 + 7

t = int(input())

for i in range(t):
    n = int(input())
    s = list(input().rstrip())

    arr = []

    st = s[0]
    c = 0
    for i in range(len(s)):
        if s[i] != st:
            arr.append(c)
            st = s[i]
            c = 0

        c += 1

    if c > 0:
        arr.append(c)

    limit = 0
    steps = 0

    for i in range(len(arr)):
        limit += 1
        if arr[i] > 1:
            red = arr[i] - 1
            gh = min(red, limit)
            arr[i] -= gh
            limit -= gh
            steps += gh

    ans = math.ceil((len(arr) + steps) / 2)
    print(ans)
