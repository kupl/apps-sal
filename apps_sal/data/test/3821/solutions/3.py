
n=int(input())

L=list(map(float,input().split()))

L.sort(reverse=True)
ans1=0.0
F=[]
Q=[]
i=0
while(i<n):
    ans2=0
    x=L[i]
    for j in range(len(F)):
        ans2+=F[j]*(1-L[i])
        x*=1-L[Q[j]]
    ans2+=x
    if(ans2>ans1):
        F.append(L[i])
        Q.append(i)
        x=1
        for j in range(len(F)-1):
            F[j]*=1-L[i]
            x*=1-L[Q[j]]
        F[-1]*=x
    ans1=max(ans2,ans1)
    i+=1

print(ans1)

