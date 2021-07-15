N=int(input())
i=1
ans=1000000000000
while i*i<=N:
    if N%i==0:
        x=i
        y=N//i
        ans=min(ans,max(len(str(x)),len(str(y))))
    i+=1
print(ans)

