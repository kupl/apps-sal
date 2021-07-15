n=int(input())
P=list(map(int,input().split()))
count=0
for i in range(1,n-1):
  if P[i-1]>P[i] and P[i]>P[i+1]:
    count+=1
  elif P[i-1]<P[i] and P[i]<P[i+1]:
    count+=1
print(count)
