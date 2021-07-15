a,b=list(map(int,input().split()))
n=0

for y in range(a+1):
  for z in range(a+1):
      p=b-y-z
      if 0<=p and p<=a:
        n+=1
print(n)
      

