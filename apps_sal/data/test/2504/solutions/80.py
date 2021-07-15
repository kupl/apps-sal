from scipy.sparse import*
f=csgraph.johnson
n,m,l,*t=map(int,open(0).read().split())
m*=3
[*map(print,f(f(csr_matrix((t[2:m:3],(t[:m:3],t[1:m:3])),[n+1]*2),0)<=l)[t[m+1::2],t[m+2::2]].clip(0,n)%n-1)]
