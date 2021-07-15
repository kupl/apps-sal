import sys
input=lambda: sys.stdin.readline().rstrip()
n,m,l,r=list(map(int,input().split()))
mod=998244353
if (n*m)%2==1:
  b,w=(n*m)//2+1,(n*m)//2
else:
  b,w=(n*m)//2,(n*m)//2

if (r-l+1)%2==0:
  e,o=(r-l+1)//2,(r-l+1)//2
else:
  if l%2==1:
    e,o=(r-l+1)//2,(r-l+1)//2+1
  else:
    e,o=(r-l+1)//2+1,(r-l+1)//2

be=(pow(e+o,b,mod)+pow(e-o,b,mod))*pow(2,mod-2,mod)
bo=(pow(e+o,b,mod)-pow(e-o,b,mod))*pow(2,mod-2,mod)
we=(pow(e+o,w,mod)+pow(e-o,w,mod))*pow(2,mod-2,mod)
wo=(pow(e+o,w,mod)-pow(e-o,w,mod))*pow(2,mod-2,mod)

if (n*m)%2==1:
  print(pow(r-l+1,n*m,mod))
else:
  print((be*we+bo*wo)%mod)


