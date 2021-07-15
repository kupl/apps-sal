#!/usr/bin/env python3
import sys
input = sys.stdin.readline

n = int(input())
a = [int(item) for item in input().split()]
a.sort()

ans = [-1] * n
num = 0
if n % 2 == 1:
    for i in range(0,n,2):
        ans[i] = a.pop()
    for i in range(1,n,2):
        if ans[i-1] > a[-1] < ans[i+1]:
            num += 1
        ans[i] = a.pop()
    print(num)
    print(*ans)
else:
    for i in range(0,n,2):
        ans[i] = a.pop()
    ans[-1] = a.pop()
    for i in range(1,n-1,2):
        if ans[i-1] > a[-1] < ans[i+1]:
            num += 1
        ans[i] = a.pop()
    print(num)
    print(*ans)
