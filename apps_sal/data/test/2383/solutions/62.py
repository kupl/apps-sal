n=int(input())
a=list(map(int,input().split()))
count=1
chk=False
for i in range(1,n+1):
  if a[i-1]==count:
    chk=True
    count+=1
print(n-count+1 if chk else -1)
