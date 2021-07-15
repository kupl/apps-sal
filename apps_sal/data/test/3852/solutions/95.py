# coding: utf-8
# Your code here!
import sys
read = sys.stdin.read
readline = sys.stdin.readline

n,*a = map(int, read().split())
idx = max(range(n),key=lambda i: abs(a[i]))

print(2*n-1)
for i in range(n):
    print(idx+1,i+1)
if a[idx] >= 0:
    for i in range(n-1):
        print(i+1,i+2)
else:
    for i in range(n-2,-1,-1):
        print(i+2,i+1)
