N,M=list(map(int,input().split()))
if N==M+1:
    A=N
    B=M
    ans=1
elif N+1==M:
    A=M
    B=N
    ans=1
elif N==M:
    A=N
    B=M
    ans=2
else:
    print((0))
    return
ansa=1
ansb=1
for i in range(1,A+1):
    ansa=(ansa*i)%(10**9+7)
for j in range(1,B+1):
    ansb=(ansb*j)%(10**9+7)

print(((ansa*ansb*ans)%(10**9+7)))

    

