l=int(input())
d=l.bit_length()
g=[]
for i in range(d-1):
  g.append((i+1,i+2,0))
  g.append((i+1,i+2,2**(d-i-2)))
s=1<<(d-1)
for i in range(d-1)[::-1]:
  if (1<<i)&l:
    g.append((1,d-i,s))
    s+=1<<i
print(d,len(g))
for u,v,c in g:
  print(u,v,c)
