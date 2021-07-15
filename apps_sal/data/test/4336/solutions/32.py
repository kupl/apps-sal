import math
import collections
ii = lambda : int(input())
mi = lambda : map(int,input().split())
li = lambda : list(map(int,input().split()))

w,h,x,y = mi()
ans = w * h / 2
check = 0
if x == w / 2 and y == h / 2:
    check = 1

print('{} {}'.format(ans,check))
