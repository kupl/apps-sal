N=int(input())
p=[[int(i) for i in input().split()] for i in range(N)]
p_copy=list(p)
p_copy.sort(key=lambda x:x[0]+x[1])
length=abs(p_copy[N-1][0])+abs(p_copy[N-1][1])
if length%2==0:
  edge=[1]
  a=1
  while a<length:
    edge.append(a)
    a=2*a
  edge.reverse()
else:
  edge=[]
  a=1
  while a<length:
    edge.append(a)
    a=2*a
  edge.reverse()
if len(edge)>40 or edge[len(edge)-1]>10**12:
  print((-1))
  return
w=[""]*N
for n in range(N):
  x,y=p[n][0],p[n][1]
  if (x+y)%2!=length%2:
    print((-1))
    return
  else:
    a,b=0,0
    for e in edge:
      R=abs(x-(a+e))+abs(y-(b))
      L=abs(x-(a-e))+abs(y-(b))
      U=abs(x-(a))+abs(y-(b+e))
      D=abs(x-(a))+abs(y-(b-e))
      if min([R,L,U,D])==R:
        a+=e
        w[n]+="R"
      elif min([R,L,U,D])==L:
        a+=-e
        w[n]+="L"
      elif min([R,L,U,D])==U:
        b+=e
        w[n]+="U"
      else:
        b+=-e
        w[n]+="D"
  
print((len(edge)))
map_edge=list(map(str,edge))
print((" ".join(map_edge)))
for n in range(N):
  print((w[n]))
    

