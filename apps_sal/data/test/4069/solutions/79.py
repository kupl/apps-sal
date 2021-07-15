import math
import collections
ii = lambda : int(input())
mi = lambda : map(int,input().split())
li = lambda : list(map(int,input().split()))

x,k,d = mi()
x = abs(x)

count = min(k,x//d)
k -= count
x -= d*count

if k % 2 == 0:
    print(x)
else:
    print(d-x)
