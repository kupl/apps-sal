import sys
input = sys.stdin.readline

#l = list(map(int, input().split()))
#import numpy as np
#arr = np.array([int(i) for i in input().split()])
'''
a,b=[],[]
for i in range():
    A, B = map(int, input().split())
    a.append(A)   
    b.append(B)'''

n,m=map(int,input().split())
if abs(n-m)>1:
    print(0)
    return

f=[1]
for i in range(1,max(n,m)+1):
    x=f[i-1]*i
    if x>10**9+7:
        x%=10**9+7
    f.append(x)
if n!=m:
    print(f[n]*f[m]%(10**9+7))
else:
    print(f[n]*f[m]*2%(10**9+7))
