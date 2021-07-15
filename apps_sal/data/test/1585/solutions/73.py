# coding: utf-8
# Your code here!
import sys
readline = sys.stdin.readline
read = sys.stdin.read

x,y = list(map(int,readline().split()))

ans = 0
while x <= y:
    x *= 2
    ans += 1

print(ans)




