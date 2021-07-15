n=int(input())
a=[0 for i in range(n+1)] 
# a[-1]=set 

if n%2==0:
    a[n]=1
    for i in range(n-1,0,-1):
        if i%2==0:
            a[i]=a[i+1]
        else:
            a[i]=1-a[i+1]
else:
    a[n]=1
    for i in range(n-1,0,-1):
        if i%2==1:
            a[i]=a[i+1]
        else:
            a[i]=1-a[i+1]
b=[]
c=[]
sb=0
sc=0
for i in range(1,n+1):
    if a[i]==0:
        b.append(i)
        sb+=i
    else:
        c.append(i)
        sc+=i
print(abs(sb-sc))
print(len(c),end=" ")
for i in c:
    print(i,end=" ")
print()    
        



