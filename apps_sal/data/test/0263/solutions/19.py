n=int(input())
m=int(input())
A=[int(input()) for i in range(n)]

A.sort()
ANS2=max(A)+m

while m!=0:
    x=min(A)
    i=0
    while i<n and m!=0:
        if A[i]==x:
            A[i]+=1
            i+=1
            m-=1
        else:
            break

    A.sort()

    
print(max(A),ANS2)

