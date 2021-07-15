n,m=list(map(int,input().split()))
L=[list(map(int,input().split())) for i in range(n)]
s="row"
s1="col"
if n>m :
    L1=[[0 for i in range(n)] for j in range(m)]
    for i in range(n) :
        for j in range(m) :
            L1[j][i]=L[i][j]
    L=L1
    n,m=m,n
    s,s1=s1,s
            
w=[0 for i in range(n)]
w1=[0 for i in range(m)]
for i in range(n) :
    w[i]=min(L[i])
for i in range(m) :
    for j in range(n) :
        ma=0
        ma=max(L[j][i]-w[j],ma)
    w1[i]=ma
for i in range(n) :
    for j in range(m) :
        if L[i][j]-w[i]-w1[j]!=0 :
            print(-1)
            return
otv=[]
for i in range(n) :
    otv+=[s+" "+str(i+1)]*w[i]
for i in range(m) :
    otv+=[s1+" "+str(i+1)]*w1[i]
print(len(otv))
print('\n'.join(otv))
            


    
    
        
    
    

