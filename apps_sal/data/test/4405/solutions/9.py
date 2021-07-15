n=int(input())
arr=list(map(int,input().split()))
d={}
powers=[]
for i in range(32):
    powers.append(2**i)
for i in arr:
    if i in list(d.keys()):
        d[i]+=1
    else:
        d[i]=1 
arr1=[]
for i in list(d.keys()):
    arr1.append(d[i])
arr1.sort(reverse=True)
maxx=arr1[0]
curr=arr1[0] 
for i in range(1,len(arr1)):
    if curr>2*arr1[i]:
        maxx=max(maxx,arr1[i]*(powers[i+1]-1))
        curr=arr1[i]
    else:
        maxx=max(maxx,(curr//2)*(powers[i+1]-1))
        curr=curr//2
    if curr==0:
        break
print(maxx)


