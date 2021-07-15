n=int(input())
c={}
for i in range(1,n+1):
    c[i]=0
max1=0
max2=0
for i in list(map(int,input().split())):
    if i<max1:
        if i>max2:
            c[max1]+=1
            max2=i
    else:
        c[i]-=1
        max1,max2=i,max1
m=-2
for i in c:
    if c[i]>m:
        m=c[i]
        ans=i
print(ans)

    

