n,k=map(int,input().split())

L=list(map(int,input().split()))

a=min(L)
b=max(L)
ans=10**10
F=[]
for s in range(1,1001):
    x=0
    E=[]
    for i in range(n):
        if(abs((s+i*k)-L[i])):
            x+=1
            E.append(i)
    if(x<ans):
        ans=x
        F=list(E)+[s]
print(ans)
s=F[-1]

for i in range(ans):
    if(L[F[i]]<s+F[i]*k):
        print("+",end=" ")
    else:
        print("-",end=" ")
    print(F[i]+1,abs((L[F[i]])-(s+F[i]*k)))

