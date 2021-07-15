n=int(input())
l=list(map(int,input().split()))
a=[]
for i in range(n):
  a.append(0)
for i in range(n-1):
  a[l[i]-1]+=1
for i in range(n):
  print(a[i])
