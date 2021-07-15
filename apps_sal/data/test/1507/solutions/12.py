#!/usr/bin/env python3
from sys import stdin, stdout

def rint():
    return list(map(int, stdin.readline().split()))
#lines = stdin.readlines()


n, k = rint()
s = input()
sl = {}
for i in range(len(s)):
    if not s[i] in sl:
        sl[s[i]] = [i,i]
    else:
        sl[s[i]][1] = i
cnt = 0
for i in range(len(s)):
    if sl[s[i]][0] == i:
        cnt+=1
    if cnt > k:
        print("YES")
        return
    if sl[s[i]][1] == i:
        cnt-=1

print("NO")



