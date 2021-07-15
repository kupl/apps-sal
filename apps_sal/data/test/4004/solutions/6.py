n=int(input())
A=list(map(int,input().split()))
A=sorted(set(A))

if len(A)>3:
    print(-1)

elif len(A)==3:
    if A[1]-A[0]==A[2]-A[1]:
        print(A[1]-A[0])
    else:
        print(-1)

elif len(A)==2:
    if (A[1]-A[0])%2==1:
        print(A[1]-A[0])
    else:
        print((A[1]-A[0])//2)

elif len(A)==1:
    print(0)
    


