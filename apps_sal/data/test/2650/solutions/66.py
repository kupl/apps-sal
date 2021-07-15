from heapq import*
f,g=heappush,heappop
(n,q),*z=[[*map(int,t.split())]for t in open(0)]
*x,(l,r)=eval('[[],[]],'*8**6)
for a,b in z[:n]:f(x[b][0],-a)
for t,_ in x:t and f(l,-t[0])
for c,d in z[n:]:
 a,b=z[c-1];z[c-1]=a,d;v,w=x[b];y,_=x[d];t=y and y[0]or 0;f(y,-a),f(w,-a)
 if-v[0]==a:
  while w and w[0]==v[0]:g(w),g(v)
  f(r,a);v and f(l,-v[0])
 if y[0]<t:f(l,a);t<0and f(r,-t)
 while r and l[0]==r[0]:g(l),g(r)
 print(l[0])
