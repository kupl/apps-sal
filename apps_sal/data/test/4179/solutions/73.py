n,m,c=map(int,input().split())
b=list(map(int, input().split()))
a=[list(map(int,input().split())) for i in range(n)]
count=0
for i in range(n):
  sum=c
  for j in range(m):
    sum+=b[j]*a[i][j]
  if sum>0:
    count+=1
print(count)
