import math
import collections
ii = lambda : int(input())
mi = lambda : map(int,input().split())
li = lambda : list(map(int,input().split()))

a,b,c = mi()
if a + b + c >=22:
    print('bust')
else:
    print('win')
