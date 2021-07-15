import math,sys,re,itertools,pprint,collections,copy
rs,ri,rai,raf=input,lambda:int(input()),lambda:list(map(int, input().split())),lambda:list(map(float, input().split()))

n = ri()
s = rs()
a = s.count('A')
d = s.count('D')
if a > d:
    print('Anton')
elif d > a:
    print('Danik')
else:
    print('Friendship')

