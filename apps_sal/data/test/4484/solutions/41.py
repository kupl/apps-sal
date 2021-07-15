N,M=map(int,input().split())
abs_NM=abs(N-M)
if abs_NM>1:
    print(0)
    return

p=10**9+7
ans=1
for i in range(1,N+1):
    ans=(ans*i)%p
for i in range(1,M+1):
    ans=(ans*i)%p
if abs_NM==0:
    ans=(ans*2)%p

print(ans)
