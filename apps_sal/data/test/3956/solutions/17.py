K,N = (int(i) for i in input().split())
mod,ans,kn = 998244353,[],K+N
fn,fk = [1]*kn,[1]*kn
for i in range(kn-1): fn[i+1] = (fn[i]*(i+2))%mod
def power(n,k):
	if k==1: return n
	elif k%2==0: return power((n**2)%mod,k//2)
	else: return (n*power(n,k-1))%mod
def comb(n,k):
	if n==0 or k==0 or n==k: return 1
	else: return (((fn[n-1]*fk[n-k-1])%mod)*fk[k-1])%mod
fk[-1] = power(fn[-1],mod-2)
for i in range(2,kn+1): fk[-i] = (fk[-i+1]*(kn+2-i))%mod
x = comb(kn-1,N)
for i in range(2,K+2):
	num,c,y,p = N-2,1,0,i//2
	while num>-1 and c<=p:
		if c%2: y = (y+comb(p,c)*comb(K+num-1,num))%mod
		else: y = (y-comb(p,c)*comb(K+num-1,num))%mod
		num,c = num-2,c+1
	ans.append((x-y)%mod)
for i in range(2,K+2): print(ans[i-2])
for i in range(K,1,-1): print(ans[i-2])
