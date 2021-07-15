import sys
input = sys.stdin.readline
from bisect import bisect_left

n = int(input())
x = [*map(int, input().split())]
y = [xi - yi for xi, yi in zip(x, map(int, input().split()))]
#print(y)
y.sort()
ans = 0
for i in range(n):
    k = y[i]
    a = bisect_left(y, -k+1)
    ans += n-a

print((ans - len([i for i in y if i > 0]))// 2)
