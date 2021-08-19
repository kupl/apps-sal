# Bhargey Mehta (Sophomore)
#DA-IICT, Gandhinagar
import sys
import math
import queue
import bisect
#sys.stdin = open("input.txt", "r")
MOD = 10**9 + 7
sys.setrecursionlimit(1000000)

n = int(input())
a = [True for i in range(n + 1)]
c = 1
ans = [-1 for i in range(n + 1)]
for i in range(2, n + 1):
    if a[i]:
        ans[i] = c
        for j in range(i + i, n + 1, i):
            a[j] = False
            ans[j] = c
        c += 1
print(*ans[2:])
