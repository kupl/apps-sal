N=int(input())
ans=N-1
x=1
while x*x<=N:
    if N%x==0:
        y=N//x
        ans=min(x-1+y-1,ans)
    x+=1
print(ans)

