n=int(input())
t=[int(a)*2 for a in input().split()]
v=[int(a)*2 for a in input().split()]
ma=[0]*(sum(t)+1)
a=0
for i in range(n):
  for j in range(t[i]):
    a+=1
    ma[a]=min(ma[a-1]+1,v[i])
ma[a]=0
for i in range(n)[::-1]:
  for j in range(t[i]):
    a-=1
    ma[a]=min(ma[a],ma[a+1]+1,v[i])
print((sum(ma[1:])+sum(ma[:-1]))/8)
