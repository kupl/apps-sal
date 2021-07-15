n=int(input())
a=list(map(int,input().split()))
b=[0]*n
k1=0
s=[]
for i in range (n):
    if b[i]==0:
        j=a[i]-1
        k=1
        b[i]=1
        sp=[i]
        while b[j] == 0:
            sp.append(j)
            k+=1
            j=a[j]-1
        s.append(min(k1,k))
        k1=max(k1,k)
        for u in sp:
            b[u]=k
#print(s,b,k1)
k2=max(s)
print(sum(list([x*x for x in s]))+k1*k1 + 2*k1*k2)

