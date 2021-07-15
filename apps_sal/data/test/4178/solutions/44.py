n=int(input())
l=list(map(int,input().split()))
d=True


for i in range(n-1):
  if l[i]>l[i+1]:
    l[i+1]+=1

  if l[i]>l[i+1]:
    d=False
    
if d:
  print("Yes")
else:
  print("No")
