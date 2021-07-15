n,m=map(int,input().split())
ab,cd=[list(map(int,input().split())) for _ in range(n)],[list(map(int,input().split())) for _ in range(m)]
for i in ab:
  r=[]
  for j in cd: r.append(abs(i[0]-j[0])+abs(i[1]-j[1]))
  print(r.index(min(r))+1)
