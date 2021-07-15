N,X=map(int,input().split())
m=[]
for i in range(N):
  m.append(int(input()))
print(len(m)+int((X-sum(m))/min(m)))
