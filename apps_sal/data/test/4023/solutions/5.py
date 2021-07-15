import collections as c
i,p,l,j=input,print,len,int
n,m,q=j(i()),0,c.deque()
f=q.append
for a in map(j,i().split()):
 if q:
  if a==q[-1]:q.pop()
  elif a>q[-1]:f(a);break
  else:f(a)
 else:f(a)
 m=max(m,a)
p('YES') if l(q)==0 or l(q)==1 and q[0]==m else p('NO')
