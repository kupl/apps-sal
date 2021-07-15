n=int(input())
a=[int(x) for x in input().split()]

dic1={}
dic2={}
for i in range(n):
  if i+1+a[i] not in dic1:
    dic1[i+1+a[i]]=1
  else:
    dic1[i+1+a[i]]+=1

for i in range(n):
  if i+1-a[i] not in dic2:
    dic2[i+1-a[i]]=1
  else:
    dic2[i+1-a[i]]+=1

ans=0

for i in dic1:
  if i not in dic2:
    continue

  ans+=dic1[i]*dic2[i]
print(ans)
