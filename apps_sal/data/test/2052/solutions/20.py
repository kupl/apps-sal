from itertools import *
r=lambda:list(map(int,input().split()))
w,l=r()
v=[0,*accumulate(r())]
# print(w,l)
# print(v)
print(min(v[i]-v[i-l] for i in range(l,w)))

