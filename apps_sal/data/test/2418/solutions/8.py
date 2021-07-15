import sys
input = sys.stdin.readline

n=int(input())
A=list(map(int,input().split()))

PLUS=[0]*(n-1)

for i in range(n-1):
    PLUS[i]=A[i+1]-A[i]

S=0
for p in PLUS:
    if p>0:
        S+=p

print((S+A[0]+1)//2)

Q=int(input())
for queries in range(Q):
    l,r,x=list(map(int,input().split()))

    if l>=2:
        ptemp=PLUS[l-2]
        PLUS[l-2]+=x

        if x>0:
            if PLUS[l-2]>0:
                S+=PLUS[l-2]-max(0,ptemp)
        else:
            if ptemp>0:
                S-=ptemp-max(0,PLUS[l-2])
    else:
        A[0]+=x

    if r<n:
        ptemp=PLUS[r-1]
        PLUS[r-1]-=x

        if x<0:
            if PLUS[r-1]>0:
                S+=PLUS[r-1]-max(0,ptemp)
        else:
            if ptemp>0:
                S-=ptemp-max(0,PLUS[r-1])

    print((S+A[0]+1)//2)

        
            
            
    

