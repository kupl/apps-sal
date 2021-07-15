D=list(map(int,input().split()))

D.sort()

A=D[2]-D[1]
D[1]+=A
D[0]+=A
result=A

if (D[1]-D[0])%2==0:
    result+=(D[1]-D[0])//2
else:
    result+=(D[1]-D[0])//2+2

print(result)



