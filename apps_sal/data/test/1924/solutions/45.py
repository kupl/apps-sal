def main():
  M=10**9+7
  r1,c1,r2,c2=map(int,input().split())
  n=r2+c2+2
  fac=[0]*(n+1)
  fac[0]=before=1
  for i in range(1,n+1):fac[i]=before=before*i%M
  f=lambda r,c:fac[r+c+2]*pow(fac[c+1],M-2,M)*pow(fac[r+1],M-2,M)-c-r-2
  print((f(r2,c2)-f(r2,c1-1)-f(r1-1,c2)+f(r1-1,c1-1))%M)
main()
