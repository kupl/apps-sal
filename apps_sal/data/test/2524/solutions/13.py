import sys
input = sys.stdin.readline

#n = int(input())
#l = list(map(int, input().split()))

'''
a=[]
b=[]
for i in range():
    A, B = map(int, input().split())
    a.append(A)   
    b.append(B)'''
import numpy as np
n=int(input())
a = np.array([int(i) for i in input().split()])

ans=0
for i in range(60):
    cnt=np.count_nonzero(a&1)
    ans+=(n-cnt)*cnt*(2**i)
    if ans>=10**9+7:
        ans%=(10**9+7)
    a>>=1
print(ans)
