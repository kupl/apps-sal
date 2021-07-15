import sys
n=int(input())
l=[]
c=0
for x in range(n):
  l.append(list(map(int,input().split())))
  if l[x][0]==l[x][1]:
    c+=1
    if c==3:
      print('Yes')
      return
  else:
    c=0
print('No')

