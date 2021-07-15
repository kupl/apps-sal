import sys
input = sys.stdin.readline

x = int(input())
ans = 0
m = x//11
n = x % 11
if n == 0:
    ans = 2*m
if 0 < n and n <= 6:
    ans = 2*m+1
if 6 < n:
    ans = 2*m+2
print(ans)

