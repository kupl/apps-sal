N=int(input())
A=list(map(int,input().split()))

m=0
index=-1
for i in range(0,N):
    if abs(A[i])>m:
        m=abs(A[i])
        index=i

if index==-1:
    print(0)
else:
    if A[index]>0:
        operate=[]
        for i in range(0,N):
            if i!=index:
                operate.append((index+1,i+1))
                A[i]+=A[index]

        for i in range(0,N-1):
            if A[i]>A[i+1]:
                operate.append((i+1,i+2))
                A[i+1]+=A[i]

        print(len(operate))
        for x,y in operate:
            print(x,y)
    else:
        operate=[]
        for i in range(0,N):
            if i!=index:
                operate.append((index+1,i+1))
                A[i]+=A[index]

        for i in range(N-1,0,-1):
            if A[i]<A[i-1]:
                operate.append((i+1,i))
                A[i-1]+=A[i]

        print(len(operate))
        for x,y in operate:
            print(x,y)
