def prime_factorizarion(n):
	arr = []
	temp = n
	for i in range(2, int(n**0.5)+1):
		if temp%i==0:
			cnt=0
			while temp%i==0:
				cnt+=1
				temp//=i
			arr.append([i,cnt])
	
	if temp!=1:
		arr.append([temp,1])
	
	if arr==[]:
		arr.append([n,1])
	
	return arr

def modInv(a,mod):
    return pow(a,mod-2,mod)

def nCr(n,r,mod):
    r=min(r,n-r)
    if r==0:
        return 1
    if r==1:
        return n
    numer=1
    denom=1
    for i in range(r):
        numer=(n-i)*numer%mod
        denom=(i+1)*denom%mod
    return numer*modInv(denom,mod)%mod

mod=10**9+7
N,M=map(int,input().split())

if M==1:
    print(1)
    return

prime_divisors=prime_factorizarion(M)
ans=1
for prime,num in prime_divisors:
    ans=(ans*nCr(num+N-1,num,mod))%mod
print(ans)
