n,m=list(map(int,input().split()))#kinds of food,customers
A=[0]+list(map(int,input().split()))#initial remain of i-th foods
C=[0]+list(map(int,input().split()))#costs
O=[list(map(int,input().split())) for i in range(m)]

C2=[[C[i+1],i+1] for i in range(n)]
C2.sort()

C2NOW=0

for f,d in O:
    ANS=0
    if A[f]>=d:
        ANS+=C[f]*d
        A[f]-=d
        print(ANS)
        continue
    

    else:
        ANS+=A[f]*C[f]
        d-=A[f]
        A[f]=0
        #print(ANS,f,d,C2[C2NOW])

        while d>0:
            
            if C2NOW==n:
                ANS=0
                d=0
                break
            
            if A[C2[C2NOW][1]]==0:
                C2NOW+=1
                continue
            
            if A[C2[C2NOW][1]]>=d:
                ANS+=d*C2[C2NOW][0]
                A[C2[C2NOW][1]]-=d
                d=0

            else:
                ANS+=A[C2[C2NOW][1]]*C2[C2NOW][0]
                d-=A[C2[C2NOW][1]]
                A[C2[C2NOW][1]]=0
                C2NOW+=1

        print(ANS)
                
                

