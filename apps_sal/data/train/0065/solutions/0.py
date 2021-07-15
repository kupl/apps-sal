import math
from collections import deque
from sys import stdin, stdout
from string import ascii_letters
import sys
letters = ascii_letters
input = stdin.readline
#print = stdout.write

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = [999999999] * n
    ans[0] = 1 if arr[0] == 1 else 0
    if n > 1:
        ans[1] = ans[0]
        if n > 2:
            ans[2] = ans[0]
    for i in range(n):
        if i + 1 >= n:
            continue
        if arr[i + 1] == 1:
            ans[i + 1] = min(ans[i + 1], ans[i] + 1)
            if i + 2 < n:
                ans[i + 2] = min(ans[i + 2], ans[i] + 1)
            if i + 3 < n: 
                ans[i + 3] = min(ans[i + 3], ans[i] + 1)
        else:
            ans[i + 1] = min(ans[i + 1], ans[i])
            if i + 2 < n:
                ans[i + 2] = min(ans[i + 2], ans[i])
            if i + 3 < n:
                ans[i + 3] = min(ans[i + 3], ans[i])
    print(ans[-1])

