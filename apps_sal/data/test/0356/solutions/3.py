import sys

n=int(input())
A=list(map(int,input().split()))
m=int(input())
B=list(map(int,input().split()))

i=0
j=0
x=A[0]
y=B[0]
ACHECK=0

while True:
    if x==y:
        i+=1
        j+=1
        if i==n and j==m:
            print(n-ACHECK)
            return

        elif i==n and j<m:
            print(-1)
            return

        elif i<n and j==m:
            print(-1)
            return
            
        x=A[i]
        y=B[j]

    elif x>y:
        j+=1

        if j==m:
            print(-1)
            return
        y+=B[j]

    elif x<y:
        i+=1

        if i==n:
            print(-1)
            return
        x+=A[i]
        ACHECK+=1
        



