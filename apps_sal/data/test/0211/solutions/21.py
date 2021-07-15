n,m,k=map(int,input().split())
if n-n//k>=m:print(m);return
mod=int(1e9+9)
x=n//k+m-n
r=pow(2,x+1,mod)-2
a=r*k+m-x*k
print((a%mod+mod)%mod)
