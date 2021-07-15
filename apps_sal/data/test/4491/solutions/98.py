n=int(input())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
ans=0
for i in range(n):
    ans=max(ans,sum(x[:i+1])+sum(y[i:]))
print(ans)
