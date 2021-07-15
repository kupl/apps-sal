from numpy import*
N,T,*L=map(int,open(0).read().split())
d=zeros(6010,int)
for w,v in sorted(zip(*[iter(L)]*2)):d[w:T+w]=maximum(d[w:T+w],d[:T]+v)
print(max(d))
