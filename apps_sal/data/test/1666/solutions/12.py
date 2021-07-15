x, y, a, b = [int(x) for x in input().split(' ')]

r = []
for i in range(a,x+1):
   for j in range(b,y+1):
      if i > j:
         r.append([i,j])

l = len(r)
r.sort(key=lambda z:10*l*z[0]+z[1])
print(len(r))
list(map(lambda z:print('%s %s'%(z[0],z[1])),r))
