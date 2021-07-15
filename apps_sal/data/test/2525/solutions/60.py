s=input()
q=int(input())
que=[list(map(str,input().split())) for i in range(q)]
count=0
for i in que:
  if i[0]=="1":
    count+=1
ans=[[],[]]
ak=count
for i in que:
  if i[0]=="1":
    count-=1
  else:
    if i[1]=="1":
      ans[count%2].append(i[2])
    else:
      ans[(count+1)%2].append(i[2])
if ak%2==0:
  print("".join(reversed(ans[0]))+s+"".join(ans[1]))
else:
  print("".join(reversed(ans[0]))+"".join(reversed(list(s)))+"".join(ans[1]))
