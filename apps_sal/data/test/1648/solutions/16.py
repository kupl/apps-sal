from scipy.special import comb
N,K=list(map(int,input().split()))
mod=10**9+7
red=N-K
for i in range(1,K+1):
   tmp=comb(N-K+1,i,exact=True)*comb(K-1,i-1,exact=True)%mod
   print(tmp)
