# coding: utf-8
# Your code here!
import sys
read = sys.stdin.read
readline = sys.stdin.readline

#xs,ys,xt,yt = map(int,readline().split())

s = input()

if ((s[0]==s[-1]) + len(s))&1:
    print("First")
else:
    print("Second")



