n = int(input())
x = []
for i in range(n):
  s,p=input().split()
  x.append([s,int(p),i+1])
x.sort(key=lambda x:(x[0],-x[1]))
for i in x:
  print(i[2])
