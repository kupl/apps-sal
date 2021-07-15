import math
#n,m=map(int,input().split())
from collections import Counter
#for i in range(n):
import math
#for _ in range(int(input())):
#n = int(input())
#for _ in range(int(input())):
#n = int(input())
import bisect
'''for _ in range(int(input())):

    n=int(input())

    n,k=map(int, input().split())

    arr = list(map(int, input().split()))'''
#n, m, k = [int(x) for x in input().split()]
n,m=list(map(int,input().split()))
arr=list(map(int,input().split()))
ls=[0]*(10**5+1)
pre=arr[0]
for i in range(1,n-1):
    if arr[i]!=arr[i+1]:
        ls[arr[i]]+=2 if arr[i+1]==pre else 1
        pre=arr[i]

if arr[0]!=arr[-1]:
    ls[arr[-1]]+=1
    if arr[0]!=arr[1]:
        ls[arr[0]]+=1

var=ls.index(max(ls))
mm=max(ls)
#print(ls[:4])
if m==2:
    if 1 in arr and 2 in arr:
        print(1)
    else:
        print(0)
else:
    for i in range(len(ls)):
        if ls[i] == mm:
            print(i)
            break












