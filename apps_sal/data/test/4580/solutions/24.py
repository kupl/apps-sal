N,*A=map(int,open(0).read().split())

colors = [0 for i in range(8)]
tyty = 0

for a in A:
  c = a//400
  if c>=8:
    tyty+=1
  else:
    colors[c]+=1

cNum = 8-colors.count(0)
    
minC = max(cNum,1)
maxC = cNum+tyty

print(minC,maxC)
