[n,m,k]=[int(i) for i in input().split()]
a=[0]*(k+1)
temp=[int(i) for i in input().split()]
for i in range(0,k):
    a[temp[i]]=i+1
answer=0
for z in range(0,n):
    temp=[int(i) for i in input().split()]
    for i in temp:
        answer+=a[i]
        for l in range(1,k+1):
            if a[l]<a[i]: a[l]+=1
        a[i]=1
        
print(answer)
