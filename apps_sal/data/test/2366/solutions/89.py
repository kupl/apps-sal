n=(int)(input())
a=input().split()
dict={}
ans=0
for i in range(n):
  a[i]=(int)(a[i])
  if not a[i] in dict:
    dict[a[i]]=1
  else:
    dict[a[i]]+=1
for i in dict:
  ans+=dict[i]*(dict[i]-1)//2
for i in range(n):
  print(ans-dict[a[i]]+1)
