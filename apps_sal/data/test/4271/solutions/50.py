n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))

addans=0

for i in range(n-1) :
  if a[i]+1 == a[i+1] :
    addans += c[a[i]-1]
print(sum(b)+addans)
