N=int(input())

X=[]


for i in range(1,N+1):
    count=0
    while i%2==0:
        i//=2
        count+=1
    X.append(count)

print((X.index(max(X))+1))

