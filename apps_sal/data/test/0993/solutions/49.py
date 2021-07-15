n,m=list(map(int,input().split()))
A=[int(i) for i in input().split()]
B=[0]
for i in range(n):
    B.append((B[-1]+A[i])%m)
B.sort()
cnt=1
now=0
ans=0
for i in range(1,n+1):
    if B[i]>now:
        ans+=cnt*(cnt-1)//2
        cnt=1
        now=B[i]
    else:
        cnt+=1
ans+=cnt*(cnt-1)//2
print(ans)


