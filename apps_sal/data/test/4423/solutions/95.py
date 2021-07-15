n=int(input())
l=[]
for i in range(n):
  city,point=input().split()
  point=int(point)
  l.append((city,point))

l=sorted(enumerate(l), key=lambda x:(x[1][0],-x[1][1]))

for i,(c,p) in l:
  print(i+1)
