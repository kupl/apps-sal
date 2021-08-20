import sys
from math import ceil, floor
input = sys.stdin.readline
t = int(input())
for zzz in range(t):
    s = list(input().strip())
    s.sort()
    i = 0
    j = len(s) - 1
    valid = True
    while i <= j:
        if s[i] != s[j]:
            valid = False
            break
        i += 1
        j -= 1
    if not valid:
        print(''.join([str(x) for x in s]))
    else:
        print(-1)
