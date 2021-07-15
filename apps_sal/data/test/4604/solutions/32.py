n=int(input())
l=list(map(int,input().split()))
mod=10**9+7
if n%2==0:
    d={i:2 for i in range(1,n,2)}
else:
    d={i:2 for i in range(0,n,2)}
    d[0]=1
for a in l:
    if a in d:
        d[a]-=1
    else:
        print(0)
        return
for i in d.values():
    if i!=0:
        print(0)
        return
print((2**(n//2))%mod)
