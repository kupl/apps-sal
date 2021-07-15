n,l=list(map(int,input().split()))

aji = [l+i for i in range(n)]
ans = None
sa=10**10
for i in range(n):
    sa_tmp=abs(aji[i])
    if sa>sa_tmp:
        sa=sa_tmp
        ans=sum(aji)-aji[i]
print(ans)

