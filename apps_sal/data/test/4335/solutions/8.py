# coding: utf-8
# Your code here!
import sys
n=int(input())
s=list(input())
if n%2==1:
    print("No")
    return
else:
    for i in range(n//2):
        if s[i]==s[n//2+i]:
            continue
        print("No")
        return
    print("Yes")
