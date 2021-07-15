n=int(input())
l=list(map(int,input().split()))
l=sorted(l)
l=l[::-1]
l1=[0]*n
k=0
for i in range(n) :
    if l1[i]!=1 :
        t=l[i]
        p=1
        r=0
        l1[i]==1
        V=[t]
        for j in range(n) :
            if l1[j]==0 and l[j]<t :
                t=l[j]
                l1[j]=1
                V.append(t)
                r=r+1
        for j in range(n-1,-1,-1) :
            if l1[j]!=1 :
                if l[j] in V :
                    q=V.index(l[j])+1
                    if len(V)-q+1<=l[j] :
                        c=0
                        s=-1
                        u=len(V)-q+1
                        for e in range(q-1,-1,-1) :
                            if V[e]>=u+s :
                                s=s+1
                            else :
                                c=1
                                break
                        if c==0 :
                            l1[j]=1
                            V=V[:q-1]+[l[j]]+V[q-1:]
                            
                            
                            
                            
                    
     
        k=k+1
        
print(k)
            
                
    

