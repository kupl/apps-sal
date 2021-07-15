n=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))



REVA=[None]*(n+1)

for i in range(n):
    REVA[A[i]]=i+1

top=0
ANSLIST=[]

for b in B:
    if REVA[b]>top:
        ANSLIST.append(REVA[b]-top)
        top=REVA[b]
    else:
        ANSLIST.append(0)

for ans in ANSLIST:
    print(ans,end=" ")

    

