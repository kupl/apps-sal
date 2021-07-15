n=int(input())
x=[]
y=[]
d=[]
c=0
for i in range(n):
 m=input()
 x.append(m)
k=int(input())
g=input()
l=len(g)
for j in range(l):
 for t in range(l):
  p=g[j:n-(n-t)+1]
  if p!='':
   y.append(p)
for r in y:
 if r not in d:
  d.append(r)
for s in d:
 if s in x:
  c=c+1
print(c) 
 

