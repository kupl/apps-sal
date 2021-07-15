N,*t=map(int,open(0).read().split())
t=iter(t)
print(N*(N+1)*(N+2)//6+sum([-min(a,b)*(N-max(a,b)+1) for a,b in zip(t,t)]))
