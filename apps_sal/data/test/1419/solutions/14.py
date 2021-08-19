# Bhargey Mehta (Sophomore)
#DA-IICT, Gandhinagar
import sys
import math
import queue
#sys.stdin = open("input.txt", "r")
MOD = 10**9 + 7
sys.setrecursionlimit(1000000)


def ok(w):
    i = 0
    c = 0
    l = 0
    while i < len(x):
        if c + x[i] <= w:
            c += x[i]
            i += 1
        else:
            l += 1
            c = 0
    l += 1
    return l <= n


n = int(input())
s = list(input().split())
x = []
for i in range(len(s) - 1):
    s[i] += " "
for i in range(len(s)):
    s[i] = s[i].split('-')
for i in range(len(s)):
    for j in range(len(s[i]) - 1):
        x.append(len(s[i][j]) + 1)
    x.append(len(s[i][-1]))
low = max(x)
high = sum(x) + 1
while low <= high:
    mid = (low + high) // 2
    if ok(mid):
        ans = mid
        high = mid - 1
    else:
        low = mid + 1
print(ans)
