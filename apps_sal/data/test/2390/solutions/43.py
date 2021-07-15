n,c=map(int,input().split())
l,L,m,M,C,a,x,v=[0],[0],[0],[0],0,0,[],[]
for i in range(n):X,V=map(int,input().split());x.append(X);v.append(V)
for i in range(n):C+=v[i];l.append(max(l[-1],C-x[i]));L.append(max(L[-1],C-2*x[i]))
C=0
for i in range(n)[::-1]:C+=v[i];m.append(max(m[-1],C-(c-x[i])));M.append(max(M[-1],C-2*(c-x[i])))
for i in range(n+1):a=max(a,l[i]+M[n-i],L[i]+m[n-i])
print(a)
