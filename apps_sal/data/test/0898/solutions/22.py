import math
n,m=map(int,input().split())
ans=list()
for i in range(1,int(math.sqrt(m))+1):
  if m%i==0:
    ans.append(i)
    ans.append(m//i)
ans.sort(reverse=True)
for x in ans:
  if x <= m//n:
    print(x)
    break
