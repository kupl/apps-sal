n=int(input())
a=list(map(int,input().split()))
dict={}
for i in range(n):
  if a[i] not in dict:
    dict[a[i]]=1
  else:
    dict[a[i]]+=1
ans=0
for i in dict:
  if dict[i]<i:
    ans+=dict[i]
  elif dict[i]==i:
    continue
  else:
    ans+=dict[i]-i
print(ans)
