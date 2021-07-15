n=int(input())
a=list(map(int,input().split()))
b=[0]*1000000
sp=-1

      
for i in range(n):
    sp=sp+1
    b[sp]=a[i]
    if sp>0:
        
        if ((b[sp]+b[sp-1])%2)==0:
            sp=sp-2

    

        
if sp<=0:
    print("YES")
else:
    print("NO")
    

             
             
             

