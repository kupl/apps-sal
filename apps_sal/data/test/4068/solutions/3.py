N, M, *A = list(map(int, open(0).read().split()))
Aset=set(A)
mod=10**9+7
num=[0]*(N+1)
for i in range(2):
    if not i in Aset:
        num[i]+=1
for i in range(2,N+1):
    if i in Aset:
        num[i]=0
    else:
        num[i]+=num[i-1]+num[i-2]
        num[i]%=mod
print((num[-1]%mod))

