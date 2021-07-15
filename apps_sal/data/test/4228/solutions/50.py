n,l = map(int,input().split())
q = []
p = []
ans = 0
for i in range(1,n+1):
  m = l+i-1
  q.append(m)
  ans += m
for i in range(n):
    p.append(abs(q[i]))

print(ans - q[p.index(min(p))])
