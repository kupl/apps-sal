N,M,X=list(map(int,input().split()))
A=list(map(int,list(input().split())))
countA=0
countB=0
for i in A:
    if i>X:
        countA+=1
    if i<X:
        countB+=1
if countA<countB:
    print(countA)
else:
    print(countB)

