from itertools import product
N,M=map(int,input().split())
x,y,z = [0]*N, [0]*N, [0]*N
for i in range(N):
    x[i],y[i],z[i] = map(int,input().split())

pat= product([1,-1],repeat=3)
ans=0
for v in pat:
    s = [ (v[0]*x[i]+v[1]*y[i]+v[2]*z[i]) for i in range(N)]
    s.sort(reverse=True)
    tmp=sum(s[:M])
    ans=max(ans,tmp)
print(ans)
