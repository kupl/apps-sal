#!/usr/bin/env python3
from sys import stdin, stdout

def rint():
    return list(map(int, stdin.readline().split()))
#lines = stdin.readlines()

n = int(input())

s = input()
s = "".join(["?", s, "?"])
#print(s)
flag = 0
for i in range(1,n+1):
    if s[i] is not "?":
        if s[i] is s[i-1] or s[i] is s[i+1]:
            print("No")
            return
    else:
        if s[i-1] is s[i+1]:
            flag = 1
        elif s[i-1] is "?" or s[i+1] is "?":
            flag = 1

if flag:
    print("Yes")
else:
    print("No")

