# coding: utf-8
# Your code here!
N,K=map(int,input().split())

A=list(map(float, input().split()))

low=0
high=10**9+1

while high-low!=1:
    mid=(high+low)//2
    cut_temp=0
    ans=-1
    
    for a in A:
        cut_temp+=-(-a//mid)-1
    if cut_temp>K:
        low=mid
    else:
        high=mid
    
print(high)
