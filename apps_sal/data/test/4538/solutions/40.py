n,D=list(map(int,input().split()))
count=0
for i in range(n):
  a,b=list(map(int,input().split()))
  d=(a**2+b**2)**(1/2)
  if d<=D:
    count+=1
print(count)

