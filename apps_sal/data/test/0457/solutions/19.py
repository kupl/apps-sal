x,n=list(map(int,input().split()))
primes=[]
i=2
while i*i<=x:
    if x%i==0:
        primes.append(i)
    while x%i==0:
        x//=i
    i+=1
if x>1:
    primes.append(x)
mod=1000000007
ans=1
for i in range(len(primes)):
    prod=primes[i]
    while prod<=n:
        ans*=pow(prod,n//prod-n//(prod*primes[i]),mod);
        ans%=mod
        prod*=primes[i]
print(ans)

