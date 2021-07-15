n=int(input())
a=list(map(int,input().split()))

h_max=a[0]
r=1
for ii in range(1,len(a)):
  if h_max<=a[ii]:
    r+=1
    h_max=a[ii]
print(r)

