n=int(input())
arr=list(map(int,input().split()))
temp=[None]*n
m=0
last=0
for i in range(n):
    if last>m:
        m=last
    last=arr[n-1-i]
    temp[n-1-i]=m
for i in range(len(arr)):
    if arr[i]<temp[i]+1:
        print(temp[i]+1-arr[i],end=' ')
    else:
        print(0,end=' ')
