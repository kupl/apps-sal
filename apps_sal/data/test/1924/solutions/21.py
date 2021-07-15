def main():
  M=10**9+7
  a,b,c,d=map(int,input().split())
  n=c+d+2
  fac=[0]*(n+1)
  fac[0]=lt=1
  for i in range(1,n+1):fac[i]=lt=lt*i%M
  inv=[0]*(n+1)
  inv[n]=lt=pow(fac[n],M-2,M)
  for i in range(n,0,-1):inv[i-1]=lt=lt*i%M
  comb=lambda n,k:fac[n]*inv[n-k]*inv[k]
  f=lambda r,c:fac[r+c+2]*inv[c+1]*inv[r+1]-c-r-2
  print((f(c,d)-f(c,b-1)-f(a-1,d)+f(a-1,b-1))%M)
main()
