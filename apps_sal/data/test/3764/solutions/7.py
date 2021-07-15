f=lambda:[int(x) for x in input().split()]
n,k,x=f()
L=f()

mi=min(L)
ma=max(L)
for i in range(k%128):
    L.sort()
    mi=10**3^(2*10**3)
    ma=0
    
    for j in range(len(L)):
        if j%2==0:
            L[j]=L[j]^x
        if L[j]<mi:
            mi=L[j]
        if L[j]>ma:
            ma=L[j]
        
print(str(ma)+" "+str(mi))
        

