n=int(input())
A=tuple(sorted(map(int,input().split() ),reverse=1))
z=n-2
ans=A[0]
now=1
while z:
    if z==1:print(A[now]+ans);return
    else:
        z-=2
        ans+=A[now]*2
        now+=1
print(ans)
