n,m=map(int,input().split())
c={i:0 for i in range(1,n+1)}
for a,b in [list(map(int,input().split())) for i in range(m)]:
  c[a]+=1;c[b]+=1
print(*c.values(),sep='\n')
