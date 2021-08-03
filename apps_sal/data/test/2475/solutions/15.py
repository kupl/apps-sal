# coding: utf-8
# Your code here!

import sys
sys.setrecursionlimit(10**6)
readline = sys.stdin.readline

n = int(input())
s = [int(i) for i in readline().split()]

n -= 1
ans = 0

for d in range(1, n + 1):
    a = n - d
    res = 0
    p, q = n, 0
    while a >= d:
        if a <= n - a and n % d == 0:
            break
        p -= d
        q += d
        res += s[p] + s[q]
#        print(d,a,res)
        if res > ans:
            ans = res
        a -= d

print(ans)
