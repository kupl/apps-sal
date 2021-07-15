n=int(input())
dic1={}
bokk=[]
list0=[]
for i in range(n):
  c,p=map(str,input().split())
  p=int(p)
  list0.append([c,p])
  if c not in dic1:
    dic1[c]=[]
  dic1[c].append(p)
dic1=dict(sorted(dic1.items()))
for i,k in dic1.items():
  k.sort(reverse=True)
  for j in k:
    bokk.append([i,j])
for i in bokk:
  print(list0.index(i)+1)
