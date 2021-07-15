n=int(input())
t=[]
for i in range(n-1):
  t.append(list(map(int,input().split())))


for i in range(n):
  s=0
  for j in range(i,n-1):
    s=max(t[j][1],((s-1)//t[j][2]+1)*t[j][2])+t[j][0]
  print(s)
