#!/usr/bin/env python3
from sys import stdin, stdout

def rint():
    return list(map(int, stdin.readline().split()))
#lines = stdin.readlines()

s = list(input())
n = len(s)

# i : rightmost position of left string
for i in range(0, n-1):
    #print(0,i,i+1, n)
    #print(s[0:i+1], s[i+1:])
    if s[i] == s[i+1] and s[0] != s[-1]:
        s1 = s[0:i+1][::-1]
        s2 = s[i+1:][::-1]
        s = s1 + s2

maxcnt = -1
cnt = 1
for i in range(n-1):
    if s[i] != s[i+1]:
        cnt += 1
    else:
        maxcnt = max(maxcnt, cnt)
        cnt = 1

maxcnt = max(maxcnt, cnt)
print(maxcnt)



