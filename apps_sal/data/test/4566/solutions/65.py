n,m=map(int,input().split())
c={i:0 for i in range(1,n+1)}
for _ in range(m):
  a,b=map(int,input().split())
  c[a]+=1;c[b]+=1
print(*c.values(),sep='\n')
