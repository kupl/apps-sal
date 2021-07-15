n=int(input())
arr=list(map(int,input().split()))
arr.reverse()
d={}
for i in range(len(arr)):
    if arr[i]+1 in d.keys():
        d[arr[i]]=d[arr[i]+1]+1 
    else:
        d[arr[i]]=1 
maxx=0
number=0
for i in d.keys():
    if d[i]>maxx:
        maxx=d[i]
        number=i 
arr.reverse()
curr=number
print(maxx)
for i in range(n):
    if arr[i]==curr:
        print(i+1,end=" ")
        curr+=1

