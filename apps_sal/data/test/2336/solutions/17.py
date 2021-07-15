n,m,k1=map(int,input().split())
l1=[0]*200003
for i in range(n) :
    a,b=map(int,input().split())
    l1[a]+=1
    l1[b+1]-=1
for i in range(1,200003) :
    l1[i]=l1[i-1]+l1[i]
l1[0]=0
for i in range(1,len(l1)) :
    if l1[i]>=m :
        l1[i]=l1[i-1]+1
    else :
        l1[i]=l1[i-1]
V=''
for i in range(k1) :
    a,b=map(int,input().split())
    V+=str(l1[b]-l1[a-1])+'\n'
print(V, end='')

    


