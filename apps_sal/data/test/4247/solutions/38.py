n=int(input())
a=list(map(int,input().split()))
count=0
for i in range(n-2):
  #print(a[i],a[i+1],a[i+2])
  if a[i]<a[i+1]<a[i+2] or a[i]>a[i+1]>a[i+2]:
    count+=1
print(count)
