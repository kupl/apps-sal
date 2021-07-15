import sys
input = sys.stdin.readline
n=int(input())
a=list(map(int, input().split()))
a.sort()
m=max(a)
arr=[0]*(m+1)
flag=[True]*(m+1)
ans=0
for i in range(n):
    if flag[a[i]]:
        arr[a[i]]+=1
        if not arr[a[i]]==1:
            continue
        for j in range(a[i]*2,m+1,a[i]):
            flag[j]=False
print(arr.count(1))
